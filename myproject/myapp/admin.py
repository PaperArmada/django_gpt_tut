from django.contrib import admin
from .models import Post, Profile

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Profile)