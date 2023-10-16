from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.admin.templatetags.base import InclusionAdminNode
from django.contrib.admin.views.main import SEARCH_VAR
from django.template import Library


register = Library()


def search_form(context, cl):
    """
    Display a search form for searching the list.
    """
    return {
        "request": context["request"],
        "cl": cl,
        "show_result_count": cl.result_count != cl.full_result_count,
        "search_var": SEARCH_VAR,
        "is_popup_var": IS_POPUP_VAR,
    }


@register.tag(name="htmx_search_form")
def search_form_tag(parser, token):
    return InclusionAdminNode(
        parser,
        token,
        func=search_form,
        template_name="search_form.html",
        takes_context=True,
    )
