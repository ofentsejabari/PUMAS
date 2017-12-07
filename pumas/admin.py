from django.contrib import admin

from pumas.models import User, UserLog
from .models import Document

# Register your models here.

admin.site.register(Document)
admin.site.register(User)
admin.site.register(UserLog)

