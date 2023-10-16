from django.contrib import admin

from foo.models import Foo


@admin.register(Foo)
class FooAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)