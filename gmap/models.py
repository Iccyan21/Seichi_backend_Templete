from django.db import models

class CustomerManager(models.Manager):
    def search_by_name(self, query):
        return self.filter(name__icontains=query)       
        
class Customer(models.Model):
    PraceID = models.IntegerField('場所ID', primary_key=True,unique=True,auto_created=True)
    name = models.CharField('名前', max_length=20)
    address = models.CharField('住所', max_length=50)
    lat = models.DecimalField('緯度', max_digits=8, decimal_places=6)
    lng = models.DecimalField('経度', max_digits=9, decimal_places=6)
    
    objects = CustomerManager()

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = '顧客'
        verbose_name_plural = '顧客'


