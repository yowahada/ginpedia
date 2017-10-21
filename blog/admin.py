from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('title','Distillery','ABV')
	#,'admin_image'

admin.site.register(Post, PostAdmin)