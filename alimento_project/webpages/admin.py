from django.contrib import admin
from .models import QuickOrder

# Register your models here.

class QuickOrderAdmin(admin.ModelAdmin):
    list_display = ('id','city','name','email')
    list_display_links = ('name',)
    search_fields = ('city','name')
    list_filter = ('city','name')

admin.site.register(QuickOrder,QuickOrderAdmin)
