from django.contrib import admin
from .models import Hosp


class HospAdmin(admin.ModelAdmin):
    list_display = ['col1', 'col2']


admin.site.register(Hosp, HospAdmin)
# Register your models here.
