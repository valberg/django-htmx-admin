from django.apps import AppConfig
from .sites import site


class HTMXAppConfig(AppConfig):
    name = "htmx_admin"
    verbose_name = "HTMX Admin"

    def ready(self):
        super().ready()

        # Since we're replacing the default admin site, we need to
        # register all the models that were already registered with
        # the default admin site.
        from django.contrib.admin import site as default_site
        site._registry.update(default_site._registry)

