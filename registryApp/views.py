from django.shortcuts import render,redirect
from . import models
from django.http import  HttpResponse
from . import tests

# Create your views here.

def wordwheel(request, case_id):
    """Parses the NTUSER hive and returns Wordwheel MRU entries."""
    wordwheel_list = tests.test("wordwheel")
    case = models.Case.objects.get(pk=case_id)
    for  wordwheel in wordwheel_list:
        wordwheelObj = models.Ntuser_WordWheel( last_write=wordwheel["last_write"],key=wordwheel["key"],\
        hive_name=wordwheel["hive"],Value=wordwheel["value"], data=wordwheel["data"]
        , case=case) 
        wordwheelObj.save()
    return HttpResponse("Done")

def typedURLs(request, case_id):
    url_set = tests.test("typedurls")
    
    case = models.Case.objects.get(pk=case_id)
    for url in url_set:
        typedUrlsObj = models.Ntuser_TypedUrls(url=url["url"], last_write=url["last_write"],  url_name=url["url_name"], \
        hive_name=url["hive"], case=case) 
        typedUrlsObj.save()
    return HttpResponse("Done")

def typedPaths(request, case_id):
    list_of_typedpaths = tests.test("typedpaths")
    case = models.Case.objects.get(pk=case_id)
    for pathObj in list_of_typedpaths:
        list_of_path_obj = models.Ntuser_TypedPath(last_write=pathObj["last_write"], keypathObj=pathObj["key"], vpathObjalupathObje=pathObj["value"], data=pathObj["data"], case=case)
        list_of_path_obj.save()

    return HttpResponse(list_of_typedpaths)

def recentDocuments(request, case_id):
    recentDocs = tests.test("recentdocs")
    case = models.Case.objects.get(pk=case_id)
    for docObj in recentDocs:
        list_of_Docs_obj = models.Ntuser_RecentDocs(last_write=docObj["last_write"], key=docObj["key"], key_name=docObj["key_name"], value=docObj["value"], data=docObj["data"], case=case)
        list_of_Docs_obj.save()

    return HttpResponse(recentDocs)


def RunMRU(request, case_id):
    """Parses the NTUSER hive and returns RunMRU entries. maintain the valueu of items tyyped in the RUN BOX"""
    runmru_list = tests.test("runmru")
    case = models.Case.objects.get(pk=case_id)
    for runmru in runmru_list:
        objRunMRU = models.Ntuser_Runmru(hive=runmru["hive"],last_write=runmru["last_write"], key=runmru["key"], mruorder=runmru["mruorder"], value=runmru["value"], data=runmru["data"], case=case)
        objRunMRU.save()
    return HttpResponse(runmru_list)

def RunKeys(request, case_id):
    """Parses the NTUSER hive and returns RunMRU entries. maintain the valueu of items tyyped in the RUN BOX"""
    runkeys_list = tests.test("runkeys")
    case = models.Case.objects.get(pk=case_id)
    if runkeys_list is not None:
        for runkey in runkeys_list:
            objRunKey = models.Ntuser_Runkeys(hive=runkey["hive"], last_write=runkey["last_write"], key=runkey["key"], mruorder=runkey["mruorder"], value=runkey["value"], data=runmru["data"], case=case)
            objRunKey.save()
    return HttpResponse("Done Runkey")

def mounts(request, case_id):
    """Parses the NTUSER  hives and returns mount points (MountPoints2, Map Network Drive MRU, & MountedDevices)."""
    mounts_list = tests.test("mounts")
    case = models.Case.objects.get(pk=case_id)
    if mounts_list is not None:
        for mount in mounts_list:
            objmounts = models.Ntuser_Mounts(hive=mount["hive"], last_write=mount["last_write"],  value=mount["value"], name=mount["name"], case=case)
            objmounts.save()
    return HttpResponse(mounts_list)

def systinternals(request, case_id):
    """Parses the NTUSER hive and returns accepted EULA entries for Sysinternal tools that have run on the system"""
    sysinternals_tools_list = tests.test("sysinternals")
    case = models.Case.objects.get(pk=case_id)
    if sysinternals_tools_list is not None:
        for systool in sysinternals_tools_list:
            systoolObj = models.Ntuser_SysteminternalsTools(hive=systool["hive"], last_write=systool["last_write"], key_name=systool["key_name"], case=case)
            systoolObj.save()
    return HttpResponse(sysinternals_tools_list)
