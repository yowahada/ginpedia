from django.contrib import admin
from import_export import resources
from .models import Post
from import_export.admin import ImportExportModelAdmin
from import_export import fields

admin.site.register(Post)
