from django.db import models


 
class Post(models.Model):
    """記事."""
    title = models.CharField(max_length=255)
    text = models.TextField()
 
    def __str__(self):
        return self.title
 
 
class Comment(models.Model):
    """コメント."""
    name = models.CharField(max_length=255, blank=True)
    text = models.TextField()
    target = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_publick = models.BooleanField(default=True)
 
    def __str__(self):
        return self.name
 
 
class Reply(models.Model):
    """返信コメント."""
    name = models.CharField(max_length=255, blank=True)
    text = models.TextField()
    target = models.ForeignKey(Comment, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
 
    def __str__(self):
        return self.name