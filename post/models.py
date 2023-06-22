from django.db import models
from gmap.models import Customer
from accounts.models import User
from anime.models import Anime

class Post(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.PROTECT,to_field='UserID',  related_name='users')
    PraceID = models.ForeignKey(Customer, on_delete=models.PROTECT,to_field='PraceID',  related_name='posts')
    AnimeID = models.ForeignKey(Anime, on_delete=models.PROTECT,to_field='amineid', related_name='animeid')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
