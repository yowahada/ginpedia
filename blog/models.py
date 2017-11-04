from django.db import models
from django.utils import timezone
import os

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    Distillery = models.CharField(max_length=200,blank=True)
    ABV = models.CharField(max_length=200,null=True,default='comming soon')
    Country = models.CharField(max_length=100, blank=True)
    Estimated_price = models.CharField(max_length=200,null=True ,default='comming soon')
    Flavor_text = models.TextField(null=True, default='comming soon')
    Botanical = models.TextField(default='comming soon')
    Tasting_note = models.TextField(null=True, default='comming soon')
    url = models.URLField(
            blank=True, max_length=200,null=True)
    image = models.ImageField(
            blank=True ,upload_to='document/',default='settings.MEDIA_ROOT/document/404.png')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    #管理画面に画像表示
    def admin_image(self):
        if self.image:
            return '<img src="{}" style="width:100px;height:auto;">'.format(self.image.url)
        else:
            return 'no image'
    admin_image.allow_tags = True


class Contact(models.Model):
    name = models.CharField("氏名", max_length=15,null=True)
    mail = models.EmailField("Mail", max_length=75,blank=True)
    contact_text = models.TextField("内容",max_length=300,blank=True)

    def __str__(self):
        return self.name