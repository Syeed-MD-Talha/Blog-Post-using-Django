from django.contrib import admin
from .models import BlogPost
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display=['id','img','title','content','author']
    
admin.site.register(BlogPost,BlogPostAdmin)