from django.db import models
from django.utils import timezone
import os

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    Distillery = models.CharField(max_length=200,blank=True)
    ABV = models.CharField(max_length=200,null=True,default='comming soon')
    Estimated_price = models.CharField(max_length=200,null=True ,default='comming soon')
    flavor_text = models.TextField(default='comming soon')
    Tasting_note = models.TextField(null=True, default='comming soon')
    Cocktails = models.TextField(null=True, default='comming soon')
    url = models.URLField(
            blank=True, max_length=200,null=True)
    image = models.ImageField(
            blank=True ,upload_to='document/',default='settings.MEDIA_ROOT/document/noimage.jpg')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def admin_image(self):
        if self.image:
            return '<img src="{}" style="width:100px;height:auto;">'.format(self.image.url)
            #return(self.image.url)
        else:
            return 'no image'
    admin_image.allow_tags = True