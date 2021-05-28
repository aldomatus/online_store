from django.contrib import admin

#   Models
from blog.models import Category, Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

#   Model registration
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
