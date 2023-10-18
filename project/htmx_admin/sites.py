from django.contrib import admin


class HTMXAdminSite(admin.AdminSite):
    index_template = "htmx_admin.html"
    app_index_template = "htmx_admin.html"
    # login_template = "htmx_admin.html"
    # logout_template = "htmx_admin.html"
    # password_change_template = "htmx_admin.html"
    # password_change_done_template = "htmx_admin.html"

    def index(self, request, extra_context=None):
        response = super().index(request, extra_context=extra_context)
        response.context_data["base_template"] = "admin/index.html"
        return response

    def app_index(self, request, app_label, extra_context=None):
        response = super().app_index(request, app_label, extra_context=extra_context)
        # TODO: support app specific templates
        response.context_data["base_template"] = "admin/app_index.html"
        return response


site = HTMXAdminSite(name="htmx_admin")


