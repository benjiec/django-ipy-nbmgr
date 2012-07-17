django-ipy-nbmgr
================

Alternative Django based iPython notebook manager: saves notebooks to database,
and archive old revisions.

To use, following these steps.

First apply the patch ipython.patch; this patch allows iPython to support
alternative notebook managers.

Second, use python setup.py install to install this python module.

Then, in a directory where you want to run iPython notebook server, create a
loader.py file:

```python
from django.conf import settings
settings.configure(
  DATABASES = { 'default': { 'ENGINE': 'django.db.backends.mysql', # or whatever your favorite db is
                             'NAME': '...',
                             'USER': '...',
                             'PASSWORD': '...'
                           }},
  TIME_ZONE = 'America/New_York',
)
import djnbmgr.manager

def get_notebook_manager():
  return djnbmgr.manager.NotebookManager()
```

Then you can start iPython in that directory like this

```
PYTHONPATH=. ipython notebook --nbmgr loader --ip 0.0.0.0 --pylab inline
```

You can then use iPython notebook server as usual, but your notebooks are stored in the database.

There is also a Django admin view that comes with the package. To use, put
"djnbmgr" in your INSTALLED_APPS list. The Django admin view lets you sort by
date and look at earlier versions of a notebook.

To use the Django admin view, you need to have both Django and the iPython
notebook server running, and add IPYTHON_NOTEBOOK_SERVER to your settings.py
file, and set it to the base URL of the notebook server. E.g.,
"http://server.com:8888".

This is all very preliminary; we are thinking about implementing a more
involved UI that supports users, tagging, etc, using Django. iPython notebook
has a very clean interface in terms of opening and saving notebooks, that made
this possible.


