from django.contrib import admin
from .models import Menu,Order
from django.utils.html import format_html
# Register your models here.

class MenuAdmin(admin.ModelAdmin):

    # add below method to display image of the menu item in admin panel.
    def photo(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.image.url))

    list_display = ('id','photo','name','price','category',)
    list_display_links = ('id','name','photo',)
    search_fields = ('name','price','category',)
    list_filter = ('price','category',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer','date_time',)
    list_display_links = ('id','customer',)
    search_fields = ('customer','items',)
    list_filter = ('items',)


admin.site.register(Menu,MenuAdmin)
admin.site.register(Order,OrderAdmin)