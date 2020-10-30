from django.shortcuts import render, Http404, get_object_or_404, redirect, HttpResponse, reverse
from django.template.context_processors import csrf
from website.models import Apps, Categories, Blog_Post, comment_put
from django.db.models import Q
# Create your views here.


def index(request):
    blog = Apps.objects.filter(category = 1).order_by('-id')
    ecommerce = Apps.objects.filter(category = 3).order_by('-id')
    portfolios = Apps.objects.filter(category = 2).order_by('-id')
    gallerie = Apps.objects.all().order_by('-id')
    context = {

        'blog': blog,
        'ecommerce': ecommerce,
        'portfolios': portfolios,
        'gallerie': gallerie,

    }
   
    return render(request, 'home/index.html', context)

def show_apps(request, id):
            
    post = get_object_or_404(Apps, id=id)
    art = Apps.objects.get(pk = id)
    
    context = {
         'art': art,
         'post': post,
          }
  
    return render(request, 'home/apps_details.html', context)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    gallerie = Apps.objects.all().order_by('-id')
    context = {
        'gallerie':gallerie, 
    }
    return render(request, 'home/contact.html', context)

def blog (request):
    post = Blog_Post.objects.all().order_by('-id')[:10]
    context = {
        'post': post,

    }
    return render(request, 'home/blog.html', context)

def blog_detail(request, id):

    post = get_object_or_404(Blog_Post, id=id)
    art = Blog_Post.objects.get(pk = id)
    comment = comment_put.objects.all().filter(user_put = id).order_by('-id')
    four = Blog_Post.objects.all().order_by('-id')[:4]
    
    context = {
         'art': art,
         'post': post,
         'four': four,
         'comment': comment,
          }

    return render(request, 'home/blog_detail.html', context)


def viewer(request):
    blogs = Apps.objects.all().filter(category = 1).order_by('-id')
    portfolios = Apps.objects.all().filter(category = 2).order_by('-id')
    ecommerce = Apps.objects.all().filter(category = 3).order_by('-id')

    context = {

       'blogs': blogs,
       'portfolios': portfolios,
       'ecommerce': ecommerce,

       }

    return render(request, 'home/Viewer.html', context)

def search(request): 
           all_articles = Apps.objects.all().order_by('-id')
             # to search in loggedin page
           search = request.GET.get('q')
           if search:
              
              all_articles = all_articles.filter(
                Q(title__icontains=search)  
               
              )
              #add paginator
          

           return render(request, 'home/search.html', {'all_articles': all_articles})


def about_me(request):

    context = {
    
    }

    return render(request, 'home/about_me.html', context)
