from django.contrib import admin
from blog.models import Post, BlogComment

admin.site.site_header = "iCoder Admin"
admin.site.site_title = "iCoder Admin Panel"
admin.site.index_title = "Welcome to iCoder Admin Panel"

# Register your models here.

admin.site.register((BlogComment))
@admin.register(Post)
 
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)