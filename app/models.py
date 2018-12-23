from django.db import models


class Category(models.Model):
    """カテゴリー"""
    name = models.CharField('カテゴリ名', max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    """記事"""
    title = models.CharField('タイトル', max_length=30)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """コメント"""
    text = models.CharField('コメント内容', max_length=100)
    post = models.ForeignKey(Post, verbose_name='紐づく記事', on_delete=models.PROTECT)

    def __str__(self):
        return self.text
