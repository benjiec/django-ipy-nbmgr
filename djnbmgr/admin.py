from django.contrib import admin
from djnbmgr.models import *


class NotebookAdmin(admin.ModelAdmin):
  def _name(self,obj):
    return '<a href="http://localhost:8888/'+str(obj.id)+'">'+str(obj.name)+'</a>'
  _name.short_description = 'Name'
  _name.allow_tags = True
  
  list_display = ('_name','deleted','archive','created_on','updated_on')
  list_filter = ('deleted','archive')

admin.site.register(Notebook,NotebookAdmin)


