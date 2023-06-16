from decimal import Decimal
from http.client import ImproperConnectionState
from operator import mod
from re import T
from unicodedata import name
from django.db import models



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Books(models.Model):
    status_books = [
        ('availble','availble'),
        ('rental','rental'),
        ('sold','sold'),

     ]
    
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    photo_book = models.ImageField(upload_to='photos/%y/%m/%d' 
    , null = True,blank =True )
    photo_author = models.ImageField(upload_to='photos/%y/%m/%d' 
    , null = True,blank =True )
    pages = models.IntegerField(null=True,blank = True)
    price = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    # price book to one day
    retal_price_day = models.DecimalField(max_digits=5,decimal_places=2,null = True,blank=True)
    # how match day take book?
    retal_period = models.IntegerField(null=True,blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50,choices=status_books,null=True,blank=True)
        # ربط الجدولين                                  # for delete I write PROTECT or not delete CASCADE
    catagery = models.ForeignKey(Category,on_delete=models.PROTECT,null=True,blank=True)
    
    
    def __str__(self):
        return self.title
