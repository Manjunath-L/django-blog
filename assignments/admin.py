from django.contrib import admin

# Register your models here.

from .models import About, SocialLinks


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        coutnt = About.objects.all().count()
        if coutnt == 0:
            return True
        return False

    list_display = ("about_heading", "created_at", "updated_at")
    search_fields = ("about_heading",)


class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ("platform", "link")
    search_fields = ("platform", "link")


admin.site.register(About, AboutAdmin)
admin.site.register(SocialLinks, SocialLinksAdmin)
