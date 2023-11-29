from django.contrib import admin
from . import models 


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}



@admin.register(models.Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['title', 'singer', 'producer', 'release_date', 'created', 'updated']
    search_fields = ['title', 'singer', 'producer', 'release_date']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = [
        ("دسته بندی و برجسب های ترک", {'fields': ["cat", "tags"]}),
        ("پرودوسر و خواننده", {'fields': ["producer", "singer"]}),
        ("مشخصات ترک", {'fields': ["title", "description", "file"]}),
        ("زمان بارگذاری و اسلاگ url", {'fields': ["slug", "release_date"]})
    ]
