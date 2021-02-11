from django.db import models
from gsheets import mixins
from uuid import uuid4

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")

class Person(mixins.SheetPullableMixin, models.Model):
    spreadsheet_id = '11t5VZMoH0W6j-Gq6loViL-Na6t2i4PyqgOzGTWtK7fE'
    sheet_name = 'design'
    model_id_field = 'id'
    
    id = models.CharField(primary_key=True, max_length=255, default=uuid4)
    title = models.CharField(max_length=127)
    url = models.CharField(max_length=500)
    description = models.CharField(max_length=127, null=True, blank=True, default=None)
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
    read_more = models.BooleanField(null=False, default=False)

    def __str__(self):
        return f'{self.title} {self.description} // {self.technology} ({self.id})'
