from django.shortcuts import render

# Create your views here.
def get_forum_page(request):
    return render(request, 'forum/forumpage.html')