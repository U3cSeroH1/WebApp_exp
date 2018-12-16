from django.contrib import admin
from comment.models import Reply, Post, Comment

# Register your models here.
admin.site.register(Reply)
admin.site.register(Post)
admin.site.register(Comment)