from django.contrib import admin
from .models import Event, News, Programs, Products, ProductsCategory


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    list_filter = ('description', 'created_at', 'updated_at')
    search_fields = ('description', 'created_at', 'updated_at')

admin.site.register (News, NewsAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    list_filter = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'created_at', 'updated_at')

admin.site.register (Event, EventAdmin)

class ProgramsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    list_filter = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'created_at', 'updated_at')

admin.site.register (Programs, ProgramsAdmin)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'note', 'created_at', 'updated_at')
    list_filter = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'created_at', 'updated_at')

admin.site.register (Products, ProductsAdmin)

class ProductsCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'created_at', 'updated_at')
    list_filter = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'created_at', 'updated_at')

admin.site.register (ProductsCategory, ProductsCategoryAdmin)

