from django.shortcuts import render

def index(request):
    context = {
        'judul':'Portofolio',
        'Contrib':'Dede Febriansyah',
        'Author':'Dede',
        'nav': [
            ['/','Home']
            ['/blog','Blog']
        ]
    }
    return render(request,'index.html', context)