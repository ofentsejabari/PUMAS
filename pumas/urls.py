from django.conf.urls import url
from pumas.views import IndexView, AllProjectView, DocumentCreate, DocumentUpdate, DocumentDelete, DetailsView, \
    SearchRepository, SearchResults, LoginView, AdminView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pumas'

urlpatterns = [
    # -- music
    url(r'^$', IndexView.as_view(), name="index"),

    # -- /pumas/all-projects/
    url(r'^all-projects/$', AllProjectView.as_view(), name="all-projects"),

    # -- /pumas/project-details/<pk/
    url(r'^project-details/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="project-details"),

    # -- /pumas/project/add/
    url(r'^projects/add/$', DocumentCreate.as_view(), name="project-add"),

    # -- /pumas/project/<pk>/update/
    url(r'^projects/(?P<pk>[0-9]+)/update/$', DocumentUpdate.as_view(), name="project-update"),

    # -- /pumas/project/<pk>/delete/
    url(r'^projects/(?P<pk>[0-9]+)/delete/$', DocumentDelete.as_view(), name="project-delete"),

    # -- /pumas/search/
    url(r'^search/$', SearchRepository.as_view(), name="search"),

    # -- /pumas/result/
    url(r'^results/$', SearchResults.as_view(), name="results"),

    # -- /pumas/login/
    url(r'^login/$', LoginView.as_view(), name="login"),

    # -- /pumas/admin/
    url(r'^admin/$', AdminView.as_view(), name="admin"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)