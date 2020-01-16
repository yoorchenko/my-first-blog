from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')#var for QuerySet
    # for e in posts:
    #     print(e.title + "\n" + e.text+"\n")
    return render(request, 'blog/post_list.html', {'posts': posts})