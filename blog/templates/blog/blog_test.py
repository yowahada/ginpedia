from django.db import models

class BigCategory(models.Model):
    """大カテゴリー"""
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_latest_title(self):
        result = POST.objects.filter(
            category__parent=self).filter(
            is_publick=True).order_by('-created_at')[:5]
        return result

class SmallCategory(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(BigCategory)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_latest_post(self):
        result = POST.objects.filter(
            category=self).filter(
            is_publick=True).order_by('-created_at')[:5]
        return result

class Tag(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_leatest_post(self):
        result = POST.objects.filter(
            tag=self).filter(
            is_publick=True
        ).order_by('-created_at')[:5]
        return result

class POST(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ForeignKey(SmallCategory, null=True, blank=True)
    tag = models.ManyToManyField(Tag,blank=True)
    thumnail = models.ImageField(upload_to='document/blog', null=True, blank=True)
    is_publick = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=255,blank=True)
    text = models.TextField(blank=True)
    target = models.ForeignKey(POST)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:10]