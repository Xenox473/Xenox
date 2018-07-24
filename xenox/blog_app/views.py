from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# from .logic import *
from .models import *
# Create your views here.
def homepage(request):
    blog_list = BlogPost.objects.all()
    context = {
        "blog_list": blog_list
    }
    return render(request, 'blog_app/homepage.html', context)
