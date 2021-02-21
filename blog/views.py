from django.shortcuts import render
from blog.models import Post, Comments
from .forms import CommentForm


# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts
    }
    return render(request, 'blog.html', context)

def full_post(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comments(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = post
            )
            comment.save()
    comments = Comments.objects.filter(post=post)

    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, 'full_post.html', context)

def category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        "posts": posts,
        "category": category
    }
    return render(request, 'category.html', context)