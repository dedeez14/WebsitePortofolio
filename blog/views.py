from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'BLOG',
        'Contrib':'DEde Febriansyah',
        'Author':'Dede',
    }
    return render(request, 'index.html', context)