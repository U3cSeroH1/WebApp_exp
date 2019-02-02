from django.db import models

from register.models import User
 
class Post(models.Model):#現在は使わない
    """記事."""
    title = models.CharField(max_length=255)
    text = models.TextField()

    #target = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
 
    def __str__(self):
        return self.title
 
 
class Comment(models.Model):
    """コメント."""
    name = models.CharField(max_length=255, blank=True)#
    text = models.TextField()
    target = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    is_public = models.BooleanField(default=True)
 
    def __str__(self):
        return self.name
 
 
class Reply(models.Model):
    """返信コメント."""
    name = models.CharField(max_length=255, blank=True)
    text = models.TextField()
    target = models.ForeignKey(Comment, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
 
    def __str__(self):
        return self.name