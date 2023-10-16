from django.db import models


class Foo(models.Model):
    name = models.CharField(max_length=255)
