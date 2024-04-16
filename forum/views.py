from django.shortcuts import render
from .models import Post


# Create your views here.
def get_forum_page(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'forum/forumpage.html', context)
