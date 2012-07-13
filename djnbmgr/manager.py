"""A notebook manager that uses Django for storage. Quacks like iPython notebook manager."""

import djnbmgr.models

class NotebookManager:

    def list_notebooks(self):
        """List all notebooks in the notebook dir.
        This returns a list of dicts of the form::
            dict(notebook_id=notebook,name=name)
        """
        # XXX

    def notebook_exists(self, notebook_id):
        """Does a notebook exist?"""
        # XXX

    def get_notebook(self, notebook_id, format=u'json'):
        """Get the representation of a notebook in format by notebook_id."""
        # XXX

    def save_new_notebook(self, data, name=None, format=u'json'):
        """Save a new notebook and return its notebook_id.

        If a name is passed in, it overrides any values in the notebook data
        and the value in the data is updated to use that value.
        """
        # XXX

    def save_notebook(self, notebook_id, data, name=None, format=u'json'):
        """Save an existing notebook by notebook_id."""
        # XXX

    def delete_notebook(self, notebook_id):
        """Delete notebook by notebook_id."""
        # XXX

    def new_notebook(self):
        """Create a new notebook and return its notebook_id."""
        # XXX

    def copy_notebook(self, notebook_id):
        """Copy an existing notebook and return its notebook_id."""
        # XXX

