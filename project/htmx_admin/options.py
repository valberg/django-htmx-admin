from django.contrib.admin.options import ModelAdmin


class HTMXAdmin(ModelAdmin):
    change_list_template = "htmx_admin.html"

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        response.context_data["base_template"] = "admin/change_list.html"
        return response
