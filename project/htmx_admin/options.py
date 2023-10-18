from django.contrib.admin.options import ModelAdmin


class HTMXAdmin(ModelAdmin):
    change_list_template = "htmx_admin.html"
    change_form_template = "htmx_admin.html"

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        response.context_data["base_template"] = "admin/change_list.html"
        return response

    def render_change_form(
        self, request, context, add=False, change=False, form_url="", obj=None
    ):
        response = super().render_change_form(
            request, context, add=add, change=change, form_url=form_url, obj=obj
        )
        response.context_data["base_template"] = "admin/change_form.html"
        return response
