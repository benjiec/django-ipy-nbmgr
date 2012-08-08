from django.contrib import admin
from djnbmgr.models import *
from django.conf import settings
from djnbmgr.manager import DjangoNotebookManager

class NotebookAdmin(admin.ModelAdmin):
  def _name(self,obj):
    nbsrv = 'http://localhost:8888'
    if settings.IPYTHON_NOTEBOOK_SERVER:
      nbsrv = settings.IPYTHON_NOTEBOOK_SERVER
    return '<a href="'+str(nbsrv)+'/'+str(obj.id)+'" target="_blank">'+DjangoNotebookManager._name(obj)+'</a>'
  _name.short_description = 'Name'
  _name.allow_tags = True

  def _revisions(self,obj):
    if obj.archive:
      return '<a href="?id__exact='+str(obj.for_notebook.id)+'">Current version</a>'
    else:
      return '<a href="?archive__exact=1&for_notebook__exact='+str(obj.id)+'">Past versions</a>'
  _revisions.short_description = 'History'
  _revisions.allow_tags = True

  list_display = ('_name','deleted','archive','created_on','updated_on','_revisions')
  list_filter = ('deleted','archive')
  ordering = ('archive','deleted','-updated_on',)

admin.site.register(Notebook,NotebookAdmin)


