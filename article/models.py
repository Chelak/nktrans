from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    class Meta:
        db_table = "article"
    author = models.ForeignKey('auth.User')
    article_title = models.CharField(max_length= 200)
    aticle_content = models.TextField()
    article_created_date = models.DateTimeField(default=timezone.now)
    article_published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.article_published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.article_title

