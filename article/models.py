from django.db import models
from django.utils import timezone

# Create your models here.
#==========================================
#　models for blog's
#==========================================

class Page(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    text = models.TextField()
    description = models.CharField(max_length=255)
    #category = models.ForeignKey(SmallCategory, null=True, blank=True)
    #tag = models.ManyToManyField(Tag, blank=True)
    thumnail = models.ImageField(
        upload_to='document/blog', null=True, blank=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_publick = models.BooleanField(default=False)

    def __str__(self):
        return self.title