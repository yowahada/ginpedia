from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    Distillery = models.CharField(max_length=200,null=True)
    ABV = models.CharField(max_length=200,null=True)
    Estimated_price = models.CharField(max_length=200,null=True)
    flavor_text = models.TextField()
    Tasting_note = models.TextField(null=True)
    Cocktails = models.TextField(null=True)
    url = models.URLField(max_length=200,null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title