from django.db import models

# Create your models here.
#==========================================
#　models for blog's
#==========================================

class Page(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    description = models.CharField(max_length=255)
    #category = models.ForeignKey(SmallCategory, null=True, blank=True)
    #tag = models.ManyToManyField(Tag, blank=True)
    thumnail = models.ImageField(
        upload_to='document/blog', null=True, blank=True
    )
    is_publick = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title