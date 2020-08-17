from django.contrib import admin  # type: ignore

# Register your models here.
from .models import Value, Characteristic

admin.site.register(Value)
admin.site.register(Characteristic)
