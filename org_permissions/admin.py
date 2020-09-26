from django.contrib import admin

from .models import OrganizationPermission, OrganizationStaffGroup

admin.site.register(OrganizationPermission)
admin.site.register(OrganizationStaffGroup)
