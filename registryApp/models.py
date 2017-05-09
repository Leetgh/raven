from django.db import models

class Case(models.Model):
    """Case Details """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    reference_number = models.CharField(max_length=50, blank=False, unique=True)
    investigators_name = models.CharField(max_length=50, blank=False)
    examiners_name = models.CharField(max_length=50, blank=False)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Ntuser_Lastvisitedmru(models.Model):
    """Parses NTUSER hive and returns LastVisitedMRU, LastVisitedPidlMRU and LastVisitedPidlMRULegacy"""
    hive = models.CharField(max_length=200)
    key  = models.CharField(max_length=300)
    value = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    last_write = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)


class Ntuser_SysteminternalsTools(models.Model):
    """Parses NTUSER hive and returns LastVisitedMRU, LastVisitedPidlMRU and LastVisitedPidlMRULegacy"""
    hive = models.CharField(max_length=200)
    key_name  = models.CharField(max_length=300)
    last_write = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

    def __str__(self):
        return self.key_name

class Ntuser_Mounts(models.Model):
    """Parses the NTUSER and SYSTEM hives and returns mount points/
     (MountPoints2, Map Network Drive MRU, & MountedDevices)"""
    hive = models.CharField(max_length=200)
    last_write = models.DateField(max_length=200)
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

class Ntuser_RecentDocs(models.Model):
    """Parses the NTUSER hive and returns RecentDocs MRU entries."""
    hive = models.CharField(max_length=200)
    last_write = models.DateField(max_length=200)
    key_name = models.CharField(max_length=200)
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

class Ntuser_Runmru(models.Model):
    """Parses the NTUSER hive and returns RunMRU entries."""
    hive = models.CharField(max_length=200)
    last_write = models.CharField(max_length=200)
    key = models.CharField(max_length=200)
    mruorder = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

class Ntuser_Runkeys(models.Model):
    """Parses the NTUSER hive and returns RunKeys entries."""
    hive = models.CharField(max_length=200)
    last_write = models.CharField(max_length=200)
    key = models.CharField(max_length=200)
    mruorder = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

class Ntuser_TypedPath(models.Model):
    """Parses the NTUSER hive and returns Typed Paths entries."""
    hive = models.CharField(max_length=200)
    last_write = models.CharField(max_length=200)
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

class Ntuser_TypedUrls(models.Model):
    """Parses the NTUSER hives and returns Typed URL entries."""

    hive = models.CharField(max_length=200)
    last_write = models.CharField(max_length=200)
    url_name = models.CharField(max_length=200)
    hive_name = models.CharField(max_length=200)
    url = models.URLField()
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

class Ntuser_WordWheel(models.Model):
    """Parses the NTUSER hive and returns Wordwheel MRU entries."""
    hive = models.CharField(max_length=200)
    last_write = models.CharField(max_length=200)
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)


""" Begin of the System Hive database """

class System_Knowndlls(models.Model):
    """Store alll the Kwown DLLs obtained from the System hive"""
    hive = models.CharField(max_length=200)
    last_write = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)


class System_Mounts(models.Model):
    """Store the mounted points (MountPoints2, Map Network Drive MRU, & MountedDevices)."""
    hive = models.CharField(max_length=200)
    last_write = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

class System_Services(models.Model):
    """Store the SYSTEM hive and returns service entries."""
    hive = models.CharField(max_length=200)
    last_write = models.CharField(max_length=200)
    key_name = models.CharField(max_length=200)
    impage_path = models.CharField(max_length=200)
    type_name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    start_type = models.CharField(max_length=200)
    service_dll = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

class System_Terminal_server(models.Model):
    """Store the SYSTEM hive and returns a Terminal Server entries."""
    hive = models.CharField(max_length=200)
    last_write = models.CharField(max_length=200)
    key_name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

class System_Usbstor(models.Model):
    """Store Vendor, Make, Version and S/N USBstor entries."""
    hive = models.CharField(max_length=200)
    last_write = models.CharField(max_length=200)
    key = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200)
    unique_sn_lastwrite = models.CharField(max_length=200)
    unique_sn = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)


class System_Sysinfo(models.Model):
    """Store system information."""
    hive = models.CharField(max_length=200)
    last_write = models.CharField(max_length=200)
    os_info = models.CharField(max_length=200)
    installed_date = models.CharField(max_length=200)
    registered_owner = models.CharField(max_length=200)
    unique_sn = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)




"""Begin Software Hive"""

class Software_Activesetup(models.Model):
    """Store activesetup entries obtained from the SOFTWARE HIVE"""
    hive = models.CharField(max_length=200)
    last_write = models.CharField(max_length=200)
    key_name = models.CharField(max_length=200)
    stub_path = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)


class Software_APPINIT(models.Model):
    """Store  AppInitDLL entries obtained from the SOFTWARE HIVE"""
    hive = models.CharField(max_length=200)
    last_write = models.CharField(max_length=200)
    key = models.CharField(max_length=200)
    loadapp_data = models.CharField(max_length=200)
    appinit_data = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

class Software_BHOS(models.Model):
    """Store  AppInitDLL entries obtained from the SOFTWARE HIVE"""
    hive = models.CharField(max_length=200)
    last_write = models.DateField()
    value = models.CharField(max_length=200)
    inproc_lastwrite = models.DateField()
    appinit_data = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

class Software_Runkeys(models.Model):
    """Store  common auto run entries obtained from SOFTWARE HIVE"""
    hive = models.CharField(max_length=200)
    last_write = models.DateField()
    key_name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

class Software_Sysinfo(models.Model):
    """Store  common auto run entries obtained from SOFTWARE HIVE"""
    hive = models.CharField(max_length=200)
    last_write = models.DateField()
    os_info = models.CharField(max_length=200)
    installed_date = models.DateField()
    registered_owner = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

class Software_Userassit(models.Model):
    """Store  common auto run entries obtained from SOFTWARE HIVE"""
    hive = models.CharField(max_length=200)
    last_write = models.DateField()
    sub_key = models.CharField(max_length=200)
    runcount = models.DateField()
    windate = models.DateField()
    data = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

class Software_Winlogon(models.Model):
    """Store  winlogon entries obtained from SOFTWARE HIVE"""
    hive = models.CharField(max_length=200)
    last_write = models.DateField()
    key_name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)