from builtins import print
from django.urls.base import reverse_lazy, reverse
from django.utils import timezone
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from pumas.models import Document


class IndexView(TemplateView):
    template_name = 'pumas/index.html'




class SearchRepository(TemplateView):
    template_name = "pumas/documentSearch.html"




class LoginView(TemplateView):
    template_name = "pumas/login.html"





class AdminView(generic.ListView):
    template_name = "pumas/admin.html"
    context_object_name = 'all_documents'

    def get_queryset(self):
        return Document.objects.all()




class SearchResults(generic.ListView):
    template_name = "pumas/search-results.html"
    context_object_name = 'filter_documents' #default is object_list

    model = Document

    def get_context_data(self, **kwargs):

        # save the search query
        search_query = self.request.GET.get('query')
        filter = self.request.GET.getlist('filter[]')

        context = super(SearchResults, self).get_context_data(**kwargs)

        context['now'] = timezone.now()
        context['filter_documents'] = Document.objects.all()
        context['search_query'] = search_query

        results = []
        if search_query:
            for document in context['filter_documents']:
                flag = False

                # if you are searching by title
                if filter.__contains__('title'):
                    if document.title.lower().find(search_query.lower()) != -1:
                        print('searching by title')
                        flag = True

                elif filter.__contains__('department'):
                    if document.department.lower().find(search_query.lower()) != -1:
                        print('searching by department')
                        flag = True

                elif filter.__contains__('type'):
                    if document.type.lower().find(search_query.lower()) != -1:
                        print('searching by type')
                        flag = True

                elif filter.__contains__('authors'):
                    if document.authors.lower().find(search_query.lower()) != -1:
                        print('searching by authors')
                        flag = True

                elif filter.__contains__('owner'):
                    if document.department.lower().find(search_query.lower()) != -1:
                        print('searching by owner')
                        flag = True

                if flag:
                    results.append(document)


        context['results'] = results
        # context['total'] = len(context['filter_documents'])
        context['total'] = len(results)

        return context


# class CheckPlagiarism(generic.ListView):
#     template_name = "pumas/search-results.html"
#     context_object_name = 'filter_documents' #default is object_list
#
#     model = Document
#     # Get the existing documents
#     documents = Document.objects.all()
#     self.plagiarism_level = process_files(self.attachment.path, documents)
#     print("Plagiarism Level --> ", self.plagiarism_level)


class AllProjectView(generic.ListView):
    template_name = "pumas/all-projects.html"
    context_object_name = 'all_documents' #default is object_list

    def get_queryset(self):
        return Document.objects.all()






class DetailsView(DetailView):
    model = Document
    template_name = "pumas/project-details.html"



class DocumentCreate(CreateView):
    model = Document
    fields = ['title', 'faculty' , 'department','type','authors',
              'attachment','abstract']

class DocumentUpdate(UpdateView):
    model = Document
    fields = ['title', 'faculty' , 'department','type','authors',
              'attachment','abstract']


class DocumentDelete(DeleteView):
    model = Document
    success_url = reverse_lazy('pumas:index')








