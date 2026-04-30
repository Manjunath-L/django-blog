import re

from blogs.models import Blog, Categories
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm

# Create your views here.


@login_required(login_url="login")
def dashboard_home(request):
    category_counts = Categories.objects.all().count()
    blog_counts = Blog.objects.all().count()
    context = {
        "category_counts": category_counts,
        "blog_counts": blog_counts,
    }
    return render(request, "dashboards/dashboard_home.html", context)


def categories(request):
    return render(request, "dashboards/categories.html")


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboards:categories")
        context = {
            "form": form,
        }
        return render(request, "dashboards/add_category.html", context)
    form = CategoryForm()
    context = {
        "form": form,
    }
    return render(request, "dashboards/add_category.html", context)


def edit_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    # category = Categories.objects.get(pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("dashboards:categories")
    context = {
        "form": CategoryForm(instance=category),
        "category": category,
    }
    return render(request, "dashboards/edit_category.html", context)


def delete_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    category.delete()
    return redirect("dashboards:categories")
