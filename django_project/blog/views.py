from django.shortcuts import render

posts = [
    {
        'author': 'Ray',
        'title': 'rays post',
        'content': 'First blog content',
        'date_posted':'March 1,2019'
    },
    {
        'author': 'mel',
        'title': 'mels post',
        'content': 'second blog content',
        'date_posted': 'March 2,2019'
    },
    {
        'author': 'Suzy',
        'title': '',
        'content': 'third blog content',
        'date_posted': 'March 4,2019'
    }

]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html', {'title':'About'})



# Create your views here.
