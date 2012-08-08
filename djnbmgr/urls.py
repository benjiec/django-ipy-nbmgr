from django.conf.urls.defaults import *
from tastypie.api import Api
from djnbmgr.api import *

api = Api(api_name="api")
api.register(NotebookResource())
api.register(ArchiveResource())
api.register(TrashedResource())

urlpatterns = patterns('',
  (r'', include(api.urls)),
)

