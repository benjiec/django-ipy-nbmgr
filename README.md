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

