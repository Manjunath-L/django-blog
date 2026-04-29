from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect

from blogs.models import Blog, Categories


# Create your views here.
def posts_by_category(request, category_id):
    # fetch posts based on category_id
    posts = Blog.objects.filter(status="Published", category=category_id)
    # try:
    #     category = Categories.objects.get(id=category_id)
    # except:
    #     return redirect("home")
    category = get_object_or_404(Categories, id=category_id)
    context = {"posts": posts, "category_name": category.category_name}
    return render(request, "posts_by_category.html", context)
