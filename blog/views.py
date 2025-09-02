from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, Category

def post_list(request):
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')

    posts = Post.objects.all().order_by('-published_date')

    if search_query:
        posts = posts.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))

    if category_filter:
        posts = posts.filter(category__name=category_filter)

    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    categories = Category.objects.all()

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'categories': categories,
        'search_query': search_query,
        'category_filter': category_filter
    })
