from tastypie.resources import ModelResource
from tastypie import fields
from djnbmgr.models import Notebook

class NotebookResource(ModelResource):
  class Meta:
    queryset = Notebook.objects.filter(deleted=False,archive=False)
    resource_name = 'notebook'
    excludes = ['content',]
    ordering = ['name','updated_on','created_on']

class ArchiveResource(ModelResource):
  class Meta:
    queryset = Notebook.objects.filter(deleted=False,archive=True)
    resource_name = 'archive'
    excludes = ['content',]
    allowed_methods = ['get',]
    ordering = ['name','updated_on','created_on']
    filtering = { "for_notebook" : ('exact',) }

class TrashedResource(ModelResource):
  class Meta:
    queryset = Notebook.objects.filter(deleted=True)
    resource_name = 'trashed'
    excludes = ['content',]
    allowed_methods = ['get',]
    ordering = ['name','updated_on','created_on']

