from django.db import models


class Notebook(models.Model):
  class Meta:
    verbose_name = "Notebook"

  id = models.CharField(max_length=128,primary_key=True)
  name = models.CharField(max_length=128)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  content = models.TextField(null=True,blank=True)
  deleted = models.BooleanField(default=False)

  def __unicode__(self):
    return self.name


class NotebookHistory(models.Model):
  class Meta:
    verbose_name = "Notebook History"
    verbose_name_plural = "Notebook Histories"

  for_notebook = models.ForeignKey(Notebook)
  updated_on = models.DateTimeField(auto_now=True)
  content = models.TextField(null=True,blank=True)

  def __unicode__(self):
    return self.for_notebook.name+"/"+str(self.id)

  def save(self, *args, **kwargs):
    if self.id != None:
      raise Exception("Cannot update existing version") 
    super(NotebookHistory,self).save(*args, **kwargs)

