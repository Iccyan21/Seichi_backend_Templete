from django.db import models


class Anime(models.Model):
    amineid = models.IntegerField(primary_key=True, editable=False)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    related = models.CharField(max_length=200)

    def __str__(self):
    	return self.title

# Create your models here.
