from django.contrib import admin
#from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

# admin.site.register(item)
@admin.register(Rice,Bakery,Dairy_products,Drinks,Spices)
class ViewAdmin(admin.ModelAdmin):
    exclude = ('id', )
