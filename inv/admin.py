from django.contrib import admin

from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.


# admin.site.register(Desktop)
# admin.site.register(Mobile)

class laptopAdmin(ImportExportModelAdmin):
		pass

class DesktopAdmin(ImportExportModelAdmin):
		pass

class MobileAdmin(ImportExportModelAdmin):
		pass

# class DesktopResource(resources.ModelResource):

#     class Meta:
#         model = Desktop

# class MobileResource(resources.ModelResource):

#     class Meta:
#         model = Mobile

admin.site.register(laptop, laptopAdmin)
admin.site.register(Desktop, DesktopAdmin)
admin.site.register(Mobile, MobileAdmin)
