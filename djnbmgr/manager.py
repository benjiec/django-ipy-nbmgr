"""A notebook manager that uses Django for storage. Quacks like iPython notebook manager."""

import os
import uuid
from djnbmgr.models import Notebook

from IPython.utils.traitlets import Unicode
from IPython.nbformat import current

class NotebookManager:
  notebook_dir = os.getcwdu()

  def __init__(self):
    pass

  def list_notebooks(self):
    """List all notebooks in the notebook dir.
    This returns a list of dicts of the form::
        dict(notebook_id=notebook,name=name)
    """
    #return [dict(notebook_id=x.id,name=x.name) for x in Notebook.objects.filter(archive=False,deleted=False)]
    return [dict(notebook_id=x.id,name=x.name) for x in Notebook.objects.all()]

  def notebook_exists(self, notebook_id):
    """Does a notebook exist?"""
    n = Notebook.objects.filter(id=notebook_id)
    return len(n) == 1

  def get_notebook(self, notebook_id, format=u'json'):
    """Get the representation of a notebook in format by notebook_id."""
    if format != 'json':
      raise Exception('Only supporting JSON in Django backed notebook')
    n = Notebook.objects.get(id=notebook_id)
    return n.updated_on, n.name, n.content

  def _archive(self, notebook, format=u'json'):
    if notebook.archive == True:
      raise Exception("Cannot archive an archived copy of a notebook")
    archive = Notebook()
    archive.id = str(uuid.uuid4())
    archive.archive = True
    archive.for_notebook = notebook
    archive.name = notebook.name+" (readonly revision - "+str(notebook.updated_on)+")"
    nb = current.reads(notebook.content, format)
    nb.metadata.name = archive.name
    archive.content = current.writes(nb, format)
    archive.save()

  def save_new_notebook(self, data, name=None, format=u'json'):
    """Save a new notebook and return its notebook_id."""
    if format != 'json':
      raise Exception('Only supporting JSON in Django backed notebook')
    n = Notebook()
    n.id = str(uuid.uuid4())
    if name != None:
      n.name = name
      nb = current.reads(data.decode('utf-8'), format)
      nb.metadata.name = name
      data = current.writes(nb, format)
    else:
      nb = current.reads(data.decode('utf-8'), format)
      n.name = nb.metadata.name
    n.content = data
    n.save(force_insert=True)
    self._archive(n)
    return n.id

  def save_notebook(self, notebook_id, data, name=None, format=u'json'):
    """Save an existing notebook by notebook_id."""
    if format != 'json':
      raise Exception('Only supporting JSON in Django backed notebook')
    n = Notebook.objects.get(id=notebook_id)
    if n.archive == True:
      raise Exception('Cannot update archived copy')
    # update copy
    if name != None:
      n.name = name
      nb = current.reads(data.decode('utf-8'), format)
      nb.metadata.name = name
      data = current.writes(nb, format)
    else:
      nb = current.reads(data.decode('utf-8'), format)
      n.name = nb.metadata.name
    n.content = data
    n.save()
    self._archive(n)
    return n.id

  def delete_notebook(self, notebook_id):
    """Delete notebook by notebook_id."""
    n = Notebook.objects.get(id=notebook_id)
    n.deleted = True
    n.save()

  def new_notebook(self):
    """Create a new notebook and return its notebook_id."""
    n = Notebook()
    n.id = str(uuid.uuid4())
    n.name = 'New Notebook'
    metadata = current.new_metadata(name=n.name)
    nb = current.new_notebook(metadata=metadata)
    data = current.writes(nb, u'json')
    n.content = data
    n.save(force_insert=True)
    return n.id

  def copy_notebook(self, notebook_id):
    """Copy an existing notebook and return its notebook_id."""
    n = Notebook.objects.get(id=notebook_id)
    n.id = str(uuid.uuid4())
    n.archive = False
    n.for_notebook = None
    if n.name != None:
      n.name = n.name+' - Copy'
      nb = current.reads(n.content, format)
      nb.metadata.name = name
      data = current.writes(nb, format)
      n.content = data
    n.save(force_insert=True)
    self._archive(n)
    return n.id

