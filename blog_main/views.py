from django.http import HttpResponse
from django.shortcuts import render, redirect

from blogs.models import Blog, Categories
from assignments.models import About, SocialLinks
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


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


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegistrationForm()
    context = {"form": form}
    return render(request, "register.html", context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboards:dashboard")
    form = AuthenticationForm()
    context = {"form": form}
    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return redirect("home")
