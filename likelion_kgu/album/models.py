from django.db import models
from likelion.models import likelion
# Create your models here.
class Album(models.Model):
    document = models.ImageField(upload_to = 'image/')
    description = models.TextField(max_length=200, blank=True)
    likelion = models.ForeignKey(likelion, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.likelion.group_number