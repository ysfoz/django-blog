from os import name
from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name
        
    



class Post(models.Model):
    OPTIONS = (
        ('d','Draft'),
        ('p','Published')
    )
    title =  models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to = '')
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    publish_date=models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices=OPTIONS,default='d')
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.title
        
    