from django.contrib import admin
from djnbmgr.models import *
from django.conf import settings

class NotebookAdmin(admin.ModelAdmin):
  def _name(self,obj):
    nbsrv = 'http://localhost:8888'
    if settings.IPYTHON_NOTEBOOK_SERVER:
      nbsrv = settings.IPYTHON_NOTEBOOK_SERVER
    return '<a href="'+str(nbsrv)+'/'+str(obj.id)+'" target="_blank">'+str(obj.name)+'</a>'
  _name.short_description = 'Name'
  _name.allow_tags = True
  
  list_display = ('_name','deleted','archive','created_on','updated_on')
  list_filter = ('deleted','archive')

admin.site.register(Notebook,NotebookAdmin)


