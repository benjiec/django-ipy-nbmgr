from tastypie.resources import ModelResource
from tastypie import fields
from djnbmgr.models import Notebook
from tastypie.authorization import Authorization

TASTYPIE_DATETIME_FORMATTING = 'rfc-2822'

class NotebookResource(ModelResource):
  class Meta:
    queryset = Notebook.objects.filter(deleted=False,archive=False)
    resource_name = 'notebook'
    excludes = ['content',]
    ordering = ['name','updated_on','created_on']
    filtering = { "name" : ('icontains',) }
    authorization = Authorization()

class ArchiveResource(ModelResource):
  class Meta:
    queryset = Notebook.objects.filter(deleted=False,archive=True)
    resource_name = 'archive'
    excludes = ['content',]
    allowed_methods = ['get',]
    ordering = ['name','updated_on','created_on']
    filtering = { "for_notebook_id" : ('exact',) }
  for_notebook_id = fields.CharField(attribute='for_notebook_id',null=True)

class TrashedResource(ModelResource):
  class Meta:
    queryset = Notebook.objects.filter(deleted=True)
    resource_name = 'trashed'
    excludes = ['content',]
    allowed_methods = ['get',]
    ordering = ['name','updated_on','created_on']

