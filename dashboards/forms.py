from django import forms
from blogs.models import Categories, Blog


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            "title",
            "category",
            "featured_image",
            "short_description",
            "blog_body",
            "status",
            "is_featured",
        ]
        # fields = "__all__"
