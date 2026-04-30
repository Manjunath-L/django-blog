from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categories(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

STATUSE_CHOICES = [
    ("Draft", "Draft"),
    ("Published", "Published"),
]

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name="blogs"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    featured_image = models.ImageField(
        upload_to="featured_images/%Y/%m/%d", blank=True, null=True
    )
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(max_length=20, choices=STATUSE_CHOICES, default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
