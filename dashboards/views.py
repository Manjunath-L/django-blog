from blogs.models import Blog, Categories
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, BlogPostForm, AddUserForm , EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

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
            "form": form,
        }
        return render(request, "dashboards/edit_category.html", context)
    context = {
        "form": CategoryForm(instance=category),
        "category": category,
    }
    return render(request, "dashboards/edit_category.html", context)


def delete_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    category.delete()
    return redirect("dashboards:categories")


def posts(request):
    posts = Blog.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "dashboards/posts.html", context)


def add_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(
                commit=False
            )  # to get the post object without saving to database
            post.author = request.user  # set the author to the currently logged in user
            post.save()
            title = form.cleaned_data["title"]  # get the title from the form
            post.slug = slugify(title) + "-" + str(post.id)  # generate slug from title
            post.save(update_fields=["slug"])  # save the post with the slug
            return redirect("dashboards:posts")
        context = {
            "form": form,
        }
        return render(request, "dashboards/add_post.html", context)
    form = BlogPostForm()
    context = {
        "form": form,
    }
    return render(request, "dashboards/add_post.html", context)


def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data["title"]  # get the title from the form
            post.slug = slugify(title) + "-" + str(post.id)  # generate slug from title
            post.save()
            return redirect("dashboards:posts")
        context = {
            "form": form
        }
        return render(request, "dashboards/edit_post.html", context)
    form = BlogPostForm(instance=post)
    context = {
        "form": form,
        "post": post,
    }
    return render(request, "dashboards/edit_post.html", context)


def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect("dashboards:posts")


def users(request):
    users = User.objects.all()
    context = {
        "users": users,
    }
    return render(request, "dashboards/users.html", context)


def add_user(request):
    form = AddUserForm()
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboards:users")
        context = {
            "form": form,
        }
        return render(request, "dashboards/add_user.html", context)
    context = {
        "form": form,
    }
    return render(request, "dashboards/add_user.html", context)

def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = EditUserForm(instance=user)
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("dashboards:users")
        context = {
            "form": form,
        }
        return render(request, "dashboards/edit_user.html", context)
    context = {
        "form": form,
        "user": user,
    }
    return render(request, "dashboards/edit_user.html", context)


def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect("dashboards:users")