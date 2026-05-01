from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404, redirect

from blogs.models import Blog, Categories, Comment
from assignments.models import About, SocialLinks
from django.db.models import Q


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


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status="Published")
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST["comment"]
        comment.save()
        return HttpResponseRedirect(request.path_info) # Redirect to the same page after submitting the comment
    # comments 
    comments = Comment.objects.filter(blog=single_blog)
    

    
    try:
        about = About.objects.get()
    except:
        about = None
    social_links = SocialLinks.objects.all()
    context = {"single_blog": single_blog, "about": about, "social_links": social_links , "comments": comments}
    return render(request, "blogs.html", context)


def search_blogs(request):
    keyword = request.GET.get("keyword")
    blogos = Blog.objects.filter(
        Q(title__icontains=keyword)
        | Q(short_description__icontains=keyword)
        | Q(blog_body__icontains=keyword),
        status="Published",
    )
    context = {"blogos": blogos , "keyword": keyword}
    return render(request, "search.html", context)

