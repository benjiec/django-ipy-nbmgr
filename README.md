django-ipy-nbmgr
================

Alternative Django based iPython notebook manager: saves notebooks to database,
and archive old revisions.

To use, following these steps.

1) You need to use a development branch of iPython:

You can install this like

```
pip install -e git://github.com/benjiec/ipython.git@azurenb#egg=IPython
```

or just checkout 

```
git clone git://github.com/benjiec/ipython.git
cd ipython
git checkout azurenb
python setup.py install
```

2) Install djnbmgr (this module)

```
git clone git://github.com/benjiec/django-ipy-nbmgr
cd django-ipy-nbmgr
python setup.py install
```

3) Configure your Django app to include "djnbmgr" in INSTALLED_APPS, and add
djnbmgr.urls to your URLs. E.g.

```
urlpatterns = patterns('',
    ...
    url(r'^djnbmgr/', include('djnbmgr.urls')),
    ...
)
```

Remember to run

```
python manage.py syncdb djnbmgr
```

4) In a directory where you want to run iPython notebook server, create a
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

5) You can start iPython in that directory like this

```
PYTHONPATH=. ipython notebook --nbmgr loader --ip 0.0.0.0 --pylab inline --NotebookApp.notebook_manager_class=loader.DjangoNotebookManager
```

6) Start your Django app. You can visit the admin interface to see notebooks
from the admin.

7) Enable javascript view of the notebooks. Create a HTML page that includes
djnbmgr JS files. E.g. assuming in your Django setting, static files are in
/static/djnbmgr and your djnbmgr URLs are mapped to /djnbmgr

```
<html>
  <head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta http-equiv="Content-Language" content="en-us" />
    <!-- CSS -->
    <link href="/static/djnbmgr/css/djnbmgr.css" rel="stylesheet" type="text/css" media="screen" />
  </head>
  <body>
    <div id="main">
    </div>
    <!-- djnbmgr JS -->
    <script src="/static/djnbmgr/js/jquery-1.7.2.min.js" type="text/javascript"></script>
    <script src="/static/djnbmgr/js/handlebars-1.0.0.beta.6.js" type="text/javascript"></script>
    <script src="/static/djnbmgr/js/handlebars-templates.js" type="text/javascript"></script>
    <script src="/static/djnbmgr/js/djnbmgr.js" type="text/javascript"></script>
    <script>
      jQuery(document).ready(function() {
        window.DjangoNotebookManager(jQuery('#main'),'/djnbmgr/api/','url to your ipython server');
      })
    </script>
  </body>
</html>
```

You can also use iPython notebook server as usual, but your notebooks are
stored in the database.

