from django.shortcuts import render

posts = [
    {
        'author': 'Ray',
        'title': 'first blog',
        'content': 'First blog content',
        'date_posted':'March 1,2019'
    },
    {
        'author': 'mel',
        'title': 'second blog',
        'content': 'second blog content',
        'date_posted': 'March 2,2019'
    },
    {
        'author': 'Suzy',
        'title': 'third blog',
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
    return render(request,'blog/about.html')


# Create your views here.
