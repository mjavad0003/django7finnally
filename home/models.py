from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

class Post(models.Model):
    title  = models.CharField(max_length=255)
    excerpt  = models.TextField()
    body  = models.TextField()
    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    date  = models.DateTimeField(default=datetime.now)
    photo = models.ImageField(null=True,upload_to='photo/%y/%m/%d')
    file = models.FileField(null=True,upload_to='file/%y/%m/%d')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.TextField(null=False,blank=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body