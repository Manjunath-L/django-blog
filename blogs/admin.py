from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Categories, Blog


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"sluge": ("title",)}
    list_display = [
        "id",
        "title",
        "category",
        "author",
        "status",
        "is_featured",
        "featured_image",
        "image_preview",
    ]

    def image_preview(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" width="100" />', obj.featured_image.url)
        return "No Image"

    image_preview.short_description = "Preview"

    list_filter = ["status", "is_featured", "created_at", "updated_at"]
    search_fields = [
        "id",
        "title",
        "category__category_name",
        "status",
        "short_description",
        "blog_body",
    ]
    list_editable = ["status", "is_featured"]


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "category_name", "created_at", "updated_at"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["category_name"]


admin.site.register(Blog, BlogAdmin)
