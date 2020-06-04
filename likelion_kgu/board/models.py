from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=125)
    post_type = models.CharField(max_length=125, default="question")
    content = models.TextField()
    author = models.CharField(max_length=125, null=True)
    password = models.CharField(max_length=15)
    lookup = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.title[:20]