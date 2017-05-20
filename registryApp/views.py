from django.shortcuts import render,redirect
from . import models
from django.http import  HttpResponse
from . import tests

#Begin NTUSER View functions

def ntuser_wordwheel(request, case_id):
    """Parses the NTUSER hive and returns Wordwheel MRU entries."""
    wordwheel_list = tests.test("wordwheel")
    case = models.Case.objects.get(pk=case_id)
    for  wordwheel in wordwheel_list:
        wordwheelObj = models.Ntuser_WordWheel( last_write=wordwheel["last_write"],key=wordwheel["key"],\
        hive_name=wordwheel["hive"],Value=wordwheel["value"], data=wordwheel["data"]
        , case=case) 
        wordwheelObj.save()
    return HttpResponse("Done")

def ntuser_typedurls(request, case_id):
    url_set = tests.test("typedurls")
    
    case = models.Case.objects.get(pk=case_id)
    for url in url_set:
        typedUrlsObj = models.Ntuser_TypedUrls(url=url["url"], last_write=url["last_write"],  url_name=url["url_name"], \
        hive_name=url["hive"], case=case) 
        typedUrlsObj.save()
    return HttpResponse("Done")

def ntuser_typedpaths(request, case_id):
    list_of_typedpaths = tests.test("typedpaths")
    case = models.Case.objects.get(pk=case_id)
    for pathObj in list_of_typedpaths:
        list_of_path_obj = models.Ntuser_TypedPath(last_write=pathObj["last_write"], keypathObj=pathObj["key"], vpathObjalupathObje=pathObj["value"], data=pathObj["data"], case=case)
        list_of_path_obj.save()

    return HttpResponse(list_of_typedpaths)

def ntuser_recentdocuments(request, case_id):
    recentDocs = tests.test("recentdocs")
    case = models.Case.objects.get(pk=case_id)
    for docObj in recentDocs:
        list_of_Docs_obj = models.Ntuser_RecentDocs(last_write=docObj["last_write"], key=docObj["key"], key_name=docObj["key_name"], value=docObj["value"], data=docObj["data"], case=case)
        list_of_Docs_obj.save()

    return HttpResponse(recentDocs)


def ntuser_runmru(request, case_id):
    """Parses the NTUSER hive and returns RunMRU entries. maintain the valueu of items tyyped in the RUN BOX"""
    runmru_list = tests.test("runmru")
    case = models.Case.objects.get(pk=case_id)
    for runmru in runmru_list:
        objRunMRU = models.Ntuser_Runmru(hive=runmru["hive"],last_write=runmru["last_write"], key=runmru["key"], mruorder=runmru["mruorder"], value=runmru["value"], data=runmru["data"], case=case)
        objRunMRU.save()
    return HttpResponse(runmru_list)

def ntuser_runkeys(request, case_id):
    """Parses the NTUSER hive and returns RunMRU entries. maintain the valueu of items tyyped in the RUN BOX"""
    runkeys_list = tests.test("runkeys")
    case = models.Case.objects.get(pk=case_id)
    if runkeys_list is not None:
        for runkey in runkeys_list:
            objRunKey = models.Ntuser_Runkeys(hive=runkey["hive"], last_write=runkey["last_write"], key=runkey["key"], mruorder=runkey["mruorder"], value=runkey["value"], data=runmru["data"], case=case)
            objRunKey.save()
    return HttpResponse("Done Runkey")

def ntuser_mounts(request, case_id):
    """Parses the NTUSER  hives and returns mount points (MountPoints2, Map Network Drive MRU, & MountedDevices)."""
    mounts_list = tests.test("mounts")
    case = models.Case.objects.get(pk=case_id)
    if mounts_list is not None:
        for mount in mounts_list:
            objmounts = models.Ntuser_Mounts(hive=mount["hive"], last_write=mount["last_write"],  value=mount["value"], name=mount["name"], case=case)
            objmounts.save()
    return HttpResponse(mounts_list)

def ntuser_systinternals(request, case_id):
    """Parses the NTUSER hive and returns accepted EULA entries for Sysinternal tools that have run on the system"""
    sysinternals_tools_list = tests.test("sysinternals")
    case = models.Case.objects.get(pk=case_id)
    if sysinternals_tools_list is not None:
        for systool in sysinternals_tools_list:
            systoolObj = models.Ntuser_SysteminternalsTools(hive=systool["hive"], last_write=systool["last_write"], key_name=systool["key_name"], case=case)
            systoolObj.save()
    return HttpResponse(sysinternals_tools_list)


#Begin System View functions

def system_knowndlls(request, case_id):
    """Parses the SYSTEM hive save and returns Known DLLs."""
    knowndlls_list = tests.test("knowndlls")
    case = models.Case.objects.get(pk=case_id)
    if knowndlls_list is not None:
        for dll in knowndlls_list:
                dllObj = models.System_Knowndlls(hive=dll["hive"], last_write=dll["last_write"], name=dll["name"], value=dll["value"], case=case)
                dllObj.save()
    return HttpResponse(knowndlls_list)

def system_mounts(request, case_id):
    """Parses the NTUSER and SYSTEM hives and save  returns mount points (MountPoints2, Map Network Drive MRU, & MountedDevices).
P"""
    return ntuser_mounts(request,case_id)

def system_service(request, case_id):
    """Parses the SYSTEM hive save and returns Known DLLs."""
    services_list = tests.test("services")
    case = models.Case.objects.get(pk=case_id)
    if system_service is not None:
        for service in services_list:
                serviceObj = models.System_Services(hive=service["hive"], last_write=service["last_write"], key_name=service["key_name"], image_path=service["image_path"], \
                type_name=service["type_name"], display_name=service["display_name"], start_type=service["start_type"],\
                service_dll=service["service_dll"], case=case)
                serviceObj.save()
    return HttpResponse(services_list)

def system_system_info(request, case_id):
    """Parses the SYSTEM and SOFTWARE hive and save the return system info."""
    system_information_list = tests.test("sysinfo")
    case = models.Case.objects.get(pk=case_id)
    if system_information_list is not None:
        for info in system_information_list:
                sysinfoObj = models.System_Sysinfo(hive=info.get("hive",""), installed_date=info.get("InstallDate",""), os_info=info.get("OSInfo",""), \
                registered_owner=info.get("Owner",""),computer_name=info.get("ComputerName",""), time_zone=info.get("TimeZone",""), case=case)
                sysinfoObj.save()
    return HttpResponse(system_information_list)

def system_terminalserver(request, case_id):
    """Parses the SYSTEM hive save return terminalserver."""
    system_terminalserver_list = tests.test("terminalserver")
    case = models.Case.objects.get(pk=case_id)
    if system_terminalserver_list is not None:
        for term in system_terminalserver_list:
                systerminalObj = models.System_Terminal_server(hive=term.get("hive",""), last_write=term.get("last_write",""), key_name=term.get("key_name",""), \
                value=term.get("value",""),data=term.get("data",""),case=case)
                systerminalObj.save()
    return HttpResponse(system_terminalserver_list)

def system_usbstor(request, case_id):
    """Parses the SYSTEM hive save and return the usbstor entry."""
    system_usbstor_list = tests.test("usbstor")
    case = models.Case.objects.get(pk=case_id)
    if system_usbstor_list is not None:
        for usb in system_usbstor_list:
                usbstorObj = models.System_Usbstor(hive=usb.get("hive",""), last_write=usb.get("last_write",""), key=usb.get("key_name",""), \
                friendly_name=usb.get("friendly_name",""),unique_sn_lastwrite=usb.get("unique_sn_lastwrite",""), unique_sn =usb.get("unique_sn",""),case=case)
                usbstorObj.save()
    return HttpResponse(system_usbstor_list)


"""Begin of Sofware HIVE """


def software_activesetup(request, case_id):
    software_activesetup_list = tests.test("activesetup")
    case = models.Case.objects.get(pk=case_id)
    if software_activesetup_list is not None:
        for setup in software_activesetup_list:
                setupObj = models.Software_Activesetup(hive=setup.get("hive",""), last_write=setup.get("last_write",""), key=setup.get("key_name",""), \
                stub_path=setup.get("stub_path",""),case=case)
                setupObj.save()
    return HttpResponse(software_activesetup_list)


def software_system_info(request, case_id):
    """Parses the  SOFTWARE hive and save the return system info."""
    system_information_list = tests.test("sysinfo")
    case = models.Case.objects.get(pk=case_id)
    if system_information_list is not None:
        for info in system_information_list:
                sysinfoObj = models.Software_Sysinfo(hive=info.get("hive",""), installed_date=info.get("InstallDate",""), os_info=info.get("OSInfo",""), \
                registered_owner=info.get("Owner",""),computer_name=info.get("ComputerName",""), time_zone=info.get("TimeZone",""), case=case)
                sysinfoObj.save()
    return HttpResponse(system_information_list)

def software_appinit(request, case_id):
    """Parses the  SOFTWARE hive and save and return appinit"""
    software_appinit_list = tests.test("appinit")
    case = models.Case.objects.get(pk=case_id)
    if software_appinit_list is not None:
        for appinit in software_appinit_list:
                appinitObj = models.Software_APPINIT(hive=appinit.get("hive",""), last_write=appinit.get("last_write",""), loadapp_data=appinit.get("loadapp_data",""), \
                appinit_data=appinit.get("appinit_data",""), case=case)
                appinitObj.save()
    return HttpResponse(software_appinit_list)


def software_runkeys(request, case_id):
    """Parses the NTUSER hive and returns RunMRU entries. maintain the valueu of items tyyped in the RUN BOX"""
    runkeys_list = tests.test("runkeys")
    case = models.Case.objects.get(pk=case_id)
    if runkeys_list is not None:
        for runkey in runkeys_list:
            objRunKey = models.Software_Runkeys(hive=runkey["hive"], last_write=runkey["last_write"], key=runkey["key"], mruorder=runkey["mruorder"], value=runkey["value"], data=runmru["data"], case=case)
            objRunKey.save()
    return HttpResponse(runkeys_list)


def software_bhos(request, case_id):
    """Browser Helper Object """
    bho_list = tests.test("bhos")
    case = models.Case.objects.get(pk=case_id)
    if bho_list is not None:
        for bho in bho_list:
            bhoObj = models.Software_BHOS(hive=bho["hive"], clsids_lastwrite=bho.get("clsids_lastwrite",""), value=bho.get("value",""), \
            inproc_lastwrite=bho.get("inproc_lastwrite",""),  data=bho.get("data",""), case=case)
            bhoObj.save()
    return HttpResponse(bho_list)


# Todo: come back to fix the error in decoding some of the values 
def software_userassist(request, case_id):
    """ Process user assist """
    userassist_list = tests.test("userassist")
    case = models.Case.objects.get(pk=case_id)
    if userassist_list is not None:
        for assist in userassist_list:
            assistObj = models.Software_Userassit(hive=assist.get("hive",""), last_write=assist.get("last_write",""), sub_key=assist.get("sub_key"), \
            runcount=assist.get("runcount",""),  windate=assist.get("windate",""), data=assist.get("data",""),case=case)
            assistObj.save()
    return HttpResponse(assistObj)

def software_winlogon(request, case_id):
    """ Process  winlogon """
    winlogon_list = tests.test("winlogon")
    case = models.Case.objects.get(pk=case_id)
    if winlogon_list is not None:
        for logon in winlogon_list:
            winlogonObj = models.Software_Winlogon(hive=logon["hive"], last_write=logon.get("last_write",""), key_name=logon.get("key_name",""), \
            value=logon.get("value",""),  data=logon.get("data",""), case=case)
            assistObj.save()
    return HttpResponse(assistObj)


