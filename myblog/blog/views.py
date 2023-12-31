from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    posts = Post.objects.all()
    posts_to_show = []

    search = request.GET.get("search")
    print(search)
    if search:
        for post in posts:
            if str(search).lower()in post.title.lower():
                posts_to_show.append(post)
            else:
                continue

    else:
        posts_to_show = posts
    return render(request, "home.html", context={"posts": posts_to_show})

def profile(request):
    return render(request,'profile.html')