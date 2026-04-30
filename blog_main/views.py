from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Blog, Categories
from assignments.models import About , SocialLinks


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status="Published").order_by(
        "-created_at"
    )
    posts = Blog.objects.filter(is_featured=False, status="Published").order_by(
        "-created_at"
    )
    try:
        about = About.objects.get()
    except:
        about = None
    social_links = SocialLinks.objects.all()
    context = {
        "featured_posts": featured_posts,
        "posts": posts,
        "about": about,
        "social_links": social_links,
    }
    return render(request, "home.html", context)
