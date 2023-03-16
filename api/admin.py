from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Note)
admin.site.register(Category)
admin.site.register(Tag)

@admin.register(Stories)
class Admin(admin.ModelAdmin):
    list_display = ['title', 'category', 'get_tags']


    def get_tags(self,obj):
        return ",".join(o for o in obj.tag.names())

