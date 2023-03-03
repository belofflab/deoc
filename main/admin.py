from django.contrib import admin

from .models import Category, Post, Case


admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}
admin.site.register(Post, PostAdmin)

class CaseAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}
admin.site.register(Case, CaseAdmin)