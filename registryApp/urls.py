from django.conf.urls import url 
from . import views


urlpatterns = [
    url(r'^ntuser/typedurls/([0-9]+)/$', views.typedURLs),
    url(r'^ntuser/wordwheel/([0-9]+)/$', views.wordwheel),
    url(r'^ntuser/typedpaths/([0-9]+)/$', views.typedPaths),
    url(r'^ntuser/recentdocuments/([0-9]+)/$', views.recentDocuments),
    url(r'^ntuser/runmru/([0-9]+)/$', views.RunMRU),
    url(r'^ntuser/runkeys/([0-9]+)/$', views.RunKeys),
    url(r'^ntuser/mount/([0-9]+)/$', views.mounts),
    url(r'^ntuser/sysinternalstools/([0-9]+)/$', views.systinternals),
    ]
