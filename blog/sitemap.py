from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse_lazy
from .models import Post, Botanicals
from article.models import Page



class PostSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.published_date

    def location(self, obj):
        return reverse_lazy('blog:detail', kwargs={'pk': obj.pk})

class PageSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return Page.objects.all()

    def lastmod(self, obj):
        return obj.is_public

    def location(self, obj):
        return reverse_lazy('article:blog_article', kwargs={'title': obj.title})

class StaticViewSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return ['blog:post_list','blog:gin_list']

    def location(self, item):
        return reverse_lazy(item)