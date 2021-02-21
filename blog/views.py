from django.shortcuts import render, HttpResponseRedirect
from blog.models import Post, Comments
from .forms import CommentForm
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created_on')
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj
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
            return HttpResponseRedirect(f'/{pk}')
    comments = Comments.objects.filter(post=post)


    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, 'full_post.html', context)

def category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "category": category
    }
    return render(request, 'category.html', context)

def Search(request):
    if request.method == 'GET':
        search_query = request.GET['search_query']
        results = Post.objects.filter(title__icontains=search_query)
        context = {
            'results': results,
            'search_query': search_query
        }
        return render(request, 'search.html', context)