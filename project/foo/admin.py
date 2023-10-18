from foo.models import Foo

import htmx_admin as admin


@admin.register(Foo)
class FooAdmin(admin.HTMXAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)
