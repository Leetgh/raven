from django.conf.urls import url 
from . import views


urlpatterns = [
    url(r'^ntuser/typedurls/([0-9]+)/$', views.ntuser_typedurls),
    url(r'^ntuser/wordwheel/([0-9]+)/$', views.ntuser_wordwheel),
    url(r'^ntuser/typedpaths/([0-9]+)/$', views.ntuser_typedpaths),
    url(r'^ntuser/recentdocuments/([0-9]+)/$', views.ntuser_recentdocuments),
    url(r'^ntuser/runmru/([0-9]+)/$', views.ntuser_runmru),
    url(r'^ntuser/runkeys/([0-9]+)/$', views.ntuser_runkeys),
    url(r'^ntuser/mount/([0-9]+)/$', views.ntuser_mounts),
    url(r'^ntuser/sysinternalstools/([0-9]+)/$', views.ntuser_systinternals),
    url(r'^system/knowndlls/([0-9]+)/$', views.system_knowndlls),
    url(r'^system/mount/([0-9]+)/$', views.system_mounts),
    url(r'^system/services/([0-9]+)/$', views.system_service),
    url(r'^system/info/([0-9]+)/$', views.system_system_info),
    url(r'^system/terminalserver/([0-9]+)/$', views.system_terminalserver),
    url(r'^system/usbstor/([0-9]+)/$', views.system_usbstor),
    url(r'^software/activesetup/([0-9]+)/$', views.software_activesetup),
    url(r'^software/systeminfo/([0-9]+)/$', views.software_system_info),
    url(r'^software/appinit/([0-9]+)/$', views.software_appinit),
    url(r'^software/runkeys/([0-9]+)/$', views.software_runkeys),
    url(r'^software/bhos/([0-9]+)/$', views.software_bhos),
    url(r'^software/userassist/([0-9]+)/$', views.software_userassist),
    url(r'^software/winlogon/([0-9]+)/$', views.software_winlogon),
     ]