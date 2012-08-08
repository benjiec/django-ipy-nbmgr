django-ipy-nbmgr
================

Alternative Django based iPython notebook manager: saves notebooks to database,
and archive old revisions.

To use, following these steps.

First, you need to use a development branch of iPython this pull request:

https://github.com/ipython/ipython/pull/2045

You can install this like

```
pip install -e git://github.com/ellisonbg/ipython.git@azurenb#egg=IPython
```

or just checkout 

```
git clone git://github.com/ellisonbg/ipython.git
cd ipython
git checkout azurenb
python setup.py install
```

Second, install djnbmgr (this module)

```
git clone git://github.com/benjiec/django-ipy-nbmgr
cd django-ipy-nbmgr
python setup.py install
```

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
from djnbmgr.manager import DjangoNotebookManager
```

Then you can start iPython in that directory like this

```
PYTHONPATH=. ipython notebook --nbmgr loader --ip 0.0.0.0 --pylab inline --NotebookApp.notebook_manager_class=loader.DjangoNotebookManager
```

You can then use iPython notebook server as usual, but your notebooks are
stored in the database.

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

