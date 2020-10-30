from django.db import models
from django.utils import timezone 

from django.shortcuts import reverse, Http404

from django.contrib.auth.models import User

from tinymce.models import HTMLField

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=200)
   
    def __str__(self):
        return self.name
class author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
   
    profile_picture = models.ImageField(blank = True, upload_to = 'Avatar', default= 'Avatar/deafult-profile-image.png')
   
    def __str__(self):
        return self.name.username


    



class Apps(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Categories, max_length=200, on_delete=models.CASCADE)
    source = models.URLField(
        max_length=128, 
        db_index=True, 
        unique=True, 
        blank=True)

    description = models.TextField(max_length=800)
    image = models.ImageField(upload_to = 'Images_Apps')
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.title


class Blog_Post(models.Model):
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, max_length=200, on_delete=models.CASCADE)
    title = models.CharField('العنوان', max_length=9500)
    avatar = models.ForeignKey(author, on_delete = models.CASCADE)
    image = models.ImageField('صورة مناسبة', upload_to = 'Images')
    source = models.CharField('المصدر', max_length=200)
    body = HTMLField()
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    publish = models.DateTimeField(default=timezone.now) 
   
    def __str__(self):
        return self.title

    
class comment_put(models.Model):

    user_comment = models.ForeignKey(User, default = None, on_delete = models.CASCADE)
    user_put = models.ForeignKey(Blog_Post, on_delete = models.CASCADE)
    avatar_commenter = models.ForeignKey(author, on_delete = models.CASCADE)
    comment = models.TextField(max_length = 500)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
   
    def __str__(self):
        return self.comment