from django.db import models
from django.contrib.auth.models import User
from  django.core.serializers import serialize
import json

class ArticleQuerySet(models.QuerySet):
    def serialize(self):
        list_value = list(self.values("id","author","title","post"))
        return json.dumps(list_value)

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model,using=self._db)


class Article(models.Model):
    title = models.CharField(max_length=127, verbose_name="heading")
    post = models.TextField(verbose_name='content')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ArticleManager() 

    def __str__(self):
        return self.title

    def serialize(self):
        data = {
            "id": self.id,
            "title": self.title,
            "author": self.author.id,
            "post": self.post,
        }
        data = json.dumps(data)
        return data

    class Meta:
        verbose_name_plural = 'Articles'
