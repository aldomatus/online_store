from django.contrib import admin
from django.contrib.admin.sites import AdminSite

#   Model
from services.models import Service


#   My models

#   Administrator class
class AdminService(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

#   Model register
admin.site.register(Service, AdminService)


