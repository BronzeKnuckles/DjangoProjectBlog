from django.shortcuts import render


posts =[
    {
        'author': 'venkypro',
        'title': 'blog post 1 ',
        'content':'FIRST POST CONTENT',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'venkypro1',
        'title': 'blog post 12 ',
        'content':'FIRST POST CONTENT1',
        'date_posted': 'August 27, 20181'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html',{'title':"ABOUT"})
