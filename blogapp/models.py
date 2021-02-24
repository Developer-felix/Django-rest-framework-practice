from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=100,null=False,blank=False)
    body = models.TextField(max_length=5000, null=False, blank=False)
    image = models.ImageField(upload_to='blog_images', blank=False)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="Date Published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Date Updated")
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)
    def __str__(self):
        return f'{self.title} -> {self.author}'
        
    