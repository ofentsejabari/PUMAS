import os

from django.core.urlresolvers import reverse
from django.db import models

from pumas.Plagiarism import process_files

TYPE_CHOICES = (
    ('THESIS/DESSERTATION','THESIS/DESSERTATION'),
    ('BSc PROJECT', 'BSc PROJECT'),
    ('JOURNALS','JOURNALS'),
)

DEPARTMENT_CHOICES = (
    ('COMPUTER SCIENCE','COMPUTER SCIENCE'),
    ('COMPUTER INFORMATION SYSTEM', 'COMPUTER INFORMATION SYSTEM'),
    ('ELECTRICAL ENGINEERING','ELECTRICAL ENGINEERING'),
)

FACULTY_CHOICES = (
    ('SCIENCE','SCIENCE'),
    ('SOCIAL SCIENCE', 'SOCIAL SCIENCE'),
    ('ENGINEERING','ENGINEERING'),
)


class Document(models.Model):

    title = models.CharField(max_length = 250)
    faculty = models.CharField(max_length=200, choices=FACULTY_CHOICES, default='fs')
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES, default='cs')
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='BSc PROJECT')
    authors = models.CharField(max_length=200)
    attachment = models.FileField(upload_to='uploads/%Y/')
    abstract = models.TextField(max_length=5000, default='')
    created = models.DateField(editable=False, auto_now_add=True)
    updated = models.DateTimeField(editable=False, auto_now=True)
    created_by = models.CharField(max_length=50, default='--')

    # Processing audit information
    PENDING, PROCESSED, FAILED = 'pending', 'approved', 'rejected'
    STATUSES = (
        (PENDING, (PENDING)),
        (PROCESSED, (PROCESSED)),
        (FAILED, (FAILED)),
    )

    status = models.CharField(max_length=40, choices=STATUSES, default=PENDING)
    plagiarism_level = models.FloatField(default=0.0)

    '''
        Some processing before you submit
    '''
    def save(self):

        # Get the existing documents
        documents = Document.objects.all()

        ext = os.path.splitext(self.attachment.name)[1]  # [0] = returns path+filename
        valid_extension = ['.pdf', '.docx', '.doc']
        if not ext in valid_extension:
            reverse("")
        else:
            if self.pk:
                if self.status != 'approved':
                    self.plagiarism_level = process_files(self.attachment.path, documents)
                    print("Plagiarism Level --> ", self.plagiarism_level)

            super(Document, self).save()

    def __unicode__(self):
        return self.title

    def __str__(self):  # -- String representation of this object
        return self.title + " - " + self.authors

    def get_absolute_url(self):
        return reverse('pumas:project-details', kwargs={'pk': self.pk})




class User(models.Model):

    userID = models.CharField(max_length=50)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class UserLog(models.Model):

    userID = models.ForeignKey(Document, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    operation = models.CharField(max_length=100)

