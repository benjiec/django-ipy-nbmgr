from django.db import models


class Notebook(models.Model):
  class Meta:
    verbose_name = "Notebook"
    app_label = "iPython Notebook"
    db_table = "djnbmgr_notebook"

  id = models.CharField(max_length=128,primary_key=True)
  name = models.CharField(max_length=128)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  content = models.TextField(null=True,blank=True)
  deleted = models.BooleanField(default=False,db_index=True)
  archive = models.BooleanField(default=False,db_index=True)
  for_notebook = models.ForeignKey('self',null=True,blank=True)

  def __unicode__(self):
    return self.name


