from django.db import models
from gmap.models import Customer

class Post(models.Model):
    PraceID = models.ForeignKey(Customer, on_delete=models.PROTECT,to_field='PraceID',  related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
