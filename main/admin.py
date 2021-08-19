from django.contrib import admin

from .models import *

class ImageInlineAdmin(admin.TabularInline):
    model = Image
    fields = ('image', )
    max_num = 2

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'published', 'active')
    list_filter = ('active', 'published')
    search_fields = ('author_name', 'comment_text')



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin,]

# Register your models here.
admin.site.register(Category)



admin.site.register(Comment, CommentAdmin)
