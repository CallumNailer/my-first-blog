from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def cv(request):
    return render(request, 'blog/cv.html', {})
