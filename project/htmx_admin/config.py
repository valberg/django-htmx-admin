from django.contrib.admin.apps import AdminConfig


class HTMXAdminConfig(AdminConfig):
    default_site = "htmx_admin.sites.HTMXAdminSite"
