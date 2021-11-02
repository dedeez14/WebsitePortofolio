from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()


    context = {
        'judul':'BLOG',
        'Contrib':'DEde Febriansyah',
        'Author':'Dede',
        'Posts': posts
    }
    return render(request, 'index.html', context)