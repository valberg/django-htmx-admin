from .sites import site as htmx_site
from django.contrib.admin.decorators import register as django_register


def register(*models, site=None):
    if site is None:
        site = htmx_site
    else:
        site = site

    return django_register(*models, site=site)
