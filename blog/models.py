from django.db import models
from django.utils import timezone
import os

class Genre(models.Model):
    genre_name = models.CharField(max_length=200,null=True,)
    content = models.TextField(null=True, default='comming soon')

    def __str__(self):
        return self.genre_name

'''Botanical for gin list'''
class Botanicals(models.Model):
    title = models.CharField(max_length=200)
    Flavor_text = models.TextField(null=True, default='comming soon')
    thumnail = models.ImageField(
        upload_to='botanical', null=True, blank=True
    )
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

'''models for gin list'''
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    Distillery = models.CharField(max_length=200,blank=True)
    ABV = models.CharField(max_length=200,null=True,default='comming soon')
    Country = models.CharField(max_length=100, blank=True)
    Estimated_price = models.CharField(max_length=200,null=True ,default='comming soon')
    genre = models.ForeignKey('Genre',null=True)
    Flavor_text = models.TextField(null=True, default='comming soon')
    botanicals = models.ManyToManyField(Botanicals, blank=True)
    Tasting_note = models.TextField(null=True, default='comming soon')
    history = models.TextField(null=True, default='comming soon')
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


    def get_next(self):
        """次の記事."""
        next_post = Post.objects.filter(
            published_date__gt=self.published_date
        ).order_by('-published_date')
        if next_post:
            return next_post.last()
        return None


    def get_prev(self):
        """前の記事."""
        prev_post = Post.objects.filter(
            published_date__lt=self.published_date
        ).order_by('-published_date')
        if prev_post:
            return prev_post.first()
        return None

'''問い合わせ用'''
class Contact(models.Model):
    name = models.CharField("氏名", max_length=15,null=True)
    mail = models.EmailField("Mail", max_length=75,blank=True)
    contact_text = models.TextField("内容",max_length=300,blank=True)

    def __str__(self):
        return self.name