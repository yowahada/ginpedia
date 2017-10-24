from django.contrib import admin
from .models import Post, Contact
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export import fields

class PostResource(resources.ModelResource):

    class Meta:
        model = Post
        widgets = {
                'published': {'format': '%d.%m.%Y'},
                }

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display = ('title','Distillery','ABV','admin_image')
	#resource_class = PostResource

admin.site.register(Post, PostAdmin)
admin.site.register(Contact)