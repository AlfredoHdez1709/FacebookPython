from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'slug', 'fecha')
	list_filter = ('fecha',)
	search_fields = ('titulo', 'cuerpo')
	prepopulated_fields = {'slug':('titulo',)}

admin.site.register(Post, PostAdmin)