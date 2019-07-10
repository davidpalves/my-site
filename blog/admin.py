from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'status',
                    'published_date', 'created_date')
    search_fields = ('title', )
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
