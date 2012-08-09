from django.contrib import admin
from djnbmgr.models import *
from djnbmgr.manager import DjangoNotebookManager

class NotebookAdmin(admin.ModelAdmin):
  def _name(self,obj):
    if obj.deleted:
      return obj.name+" (Deleted)"
    elif obj.archive:
      return obj.name+" (Archived)"
    return obj.name

  def _revisions(self,obj):
    if obj.archive:
      return '<a href="?id__exact='+str(obj.for_notebook.id)+'">Current version</a>'
    else:
      return '<a href="?archive__exact=1&for_notebook__exact='+str(obj.id)+'">Past versions</a>'
  _revisions.short_description = 'History'
  _revisions.allow_tags = True

  list_display = ('id', '_name','deleted','archive','created_on','updated_on','_revisions')
  list_filter = ('deleted','archive')
  ordering = ('archive','deleted','-updated_on',)
  exclude = ('content',)
  readonly_fields = ('for_notebook','id')

admin.site.register(Notebook,NotebookAdmin)


