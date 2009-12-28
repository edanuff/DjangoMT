from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import loader

from django.contrib.sites.models import Site
from django.contrib.auth.views import login, logout 

from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail

from models import Blog
from models import Entry
from models import Comment

NUM_IN_PAGE = 5

def set_cookie(response, key, value, expire=None):
    if expire is None:
        max_age = 365*24*60*60  #one year
    else:
        max_age = expire
    expires = datetime.strftime(datetime.utcnow() + timedelta(seconds = max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age = max_age, expires = expires, 
        domain = settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE or None)

def render_response(*args, **kwargs):
    response = kwargs.pop('response', None)
    if response == None:
        return render_to_response(*args, **kwargs)
    else:
        response.content = loader.render_to_string(*args, **kwargs)
        return response   
       
def get_style(request):
    style = settings.DEFAULT_STYLE
    if "style" in request.COOKIES:
      style = request.COOKIES["style"]
    return request.GET.get("style", style)
    
def default_page(request):
    return HttpResponse("Default Index Page")
  
def get_blog(request, blog_name):
    
    blog = None
    try:
      blog = Blog.objects.get(site_path__iendswith = blog_name)
    except Blog.DoesNotExist: 
      pass
    
    if not blog:
      raise Http404
     
    return blog
  
def archive_index(request, page = "1", blog_name = settings.DEFAULT_BLOG):
    style = get_style(request)

    blog = get_blog(request, blog_name)
    
    queryset = blog.entries.filter(class_field = "entry")
    queryset = queryset.order_by("-created_on")
 
    extra_context = {
      "style" : style,
      "blog_path" : "/" + blog_name + "/",
      "page_path" : "/" + blog_name + "/",
      "blog_name" : blog_name,
      "blog" : blog,
    }
    
    return object_list(
      request, 
      queryset,
      extra_context = extra_context,
      template_object_name = "entry",
      paginate_by = NUM_IN_PAGE, 
      page = int(page),
      template_name = settings.DEFAULT_TEMPLATE + "/archive_index.html"
    )

def archive_year(request, year, page = "1", blog_name = settings.DEFAULT_BLOG):
    style = get_style(request)

    blog = get_blog(request, blog_name)
    
    queryset = blog.entries.filter(class_field = "entry")
    queryset = queryset.filter(authored_on__year = year)
    queryset = queryset.order_by("-created_on")
    
    archive_date = datetime(int(year), 1, 1)
      
    extra_context = {
      "style" : style,
      "blog_path" : "/" + blog_name + "/",
      "page_path" : "/" + blog_name + "/" + year + "/",
      "blog_name" : blog_name,
      "blog" : blog,
      "archive_year" : year,
      "archive_date" : archive_date,
    }
    
    return object_list(
      request, 
      queryset,
      extra_context = extra_context,
      template_object_name = "entry",
      paginate_by = NUM_IN_PAGE, 
      page = int(page),
      template_name = settings.DEFAULT_TEMPLATE + "/archive_year.html"
    )

def archive_month(request, year, month, page = "1", blog_name = settings.DEFAULT_BLOG):
    style = get_style(request)

    blog = get_blog(request, blog_name)
    
    queryset = blog.entries.filter(class_field = "entry")
    queryset = queryset.filter(authored_on__year = year)
    queryset = queryset.filter(authored_on__month = month)
    queryset = queryset.order_by("-created_on")
      
    archive_date = datetime(int(year), int(month), 1)
      
    extra_context = {
      "style" : style,
      "blog_path" : "/" + blog_name + "/",
      "blog_name" : blog_name,
      "page_path" : "/" + blog_name + "/" + year + "/" + month + "/",
      "blog" : blog,
      "archive_year" : year,
      "archive_month" : month,
      "archive_date" : archive_date,
    }
    
    return object_list(
      request, 
      queryset,
      extra_context = extra_context,
      template_object_name = "entry",
      paginate_by = NUM_IN_PAGE, 
      page = int(page),
      template_name = settings.DEFAULT_TEMPLATE + "/archive_month.html"
    )

def archive_category(request, category_basename, page = "1", blog_name = settings.DEFAULT_BLOG):
    style = get_style(request)

    blog = get_blog(request, blog_name)
    
    entries_category = blog.categories.get(
      class_field = "category", 
      basename = category_basename)

    queryset = entries_category.entries.filter(class_field = "entry")
    queryset = queryset.order_by("-created_on")
      
    extra_context = {
      "style" : style,
      "blog_path" : "/" + blog_name + "/",
      "page_path" : "/" + blog_name + "/" + category_basename + "/",
      "blog_name" : blog_name,
      "blog" : blog,
      "entries_category" : entries_category,
    }
    
    return object_list(
      request, 
      queryset,
      extra_context = extra_context,
      template_object_name = "entry",
      paginate_by = NUM_IN_PAGE, 
      page = int(page),
      template_name = settings.DEFAULT_TEMPLATE + "/archive_index.html"
    )

def entry_detail(request, year, month, entry_basename, blog_name = settings.DEFAULT_BLOG):
    style = get_style(request)

    blog = get_blog(request, blog_name)
    
    if request.method == 'GET': 
      queryset = blog.entries.all()  
      
      extra_context = {
        "style" : style,
        "blog_path" : "/" + blog_name + "/",
        "page_path" : "/" + blog_name + "/" + year + "/" + month + "/" + entry_basename + ".html",
        "blog_name" : blog_name,
        "blog" : blog,
      }
      
      return object_detail(
        request, 
        queryset,
        slug = entry_basename,
        slug_field = "basename",
        extra_context = extra_context,
        template_object_name = "entry",
        template_name = settings.DEFAULT_TEMPLATE + "/entry_detail.html"
      )

    elif request.method == 'POST': 
      if not request.user.is_authenticated(): 
        return HttpResponseRedirect('/login/?next=%s' % request.path) 
      return HttpResponse("Default Index Page")


    
def page_detail(request, page_basename, blog_name = settings.DEFAULT_BLOG):
    style = get_style(request)

    blog = get_blog(request, blog_name)
    
    queryset = blog.entries.all()  
      
    extra_context = {
      "style" : style,
      "blog_path" : "/" + blog_name + "/",
      "page_path" : "/" + blog_name + "/" + page_basename + ".html",
      "blog_name" : blog_name,
      "blog" : blog,
    }
    
    return object_detail(
      request, 
      queryset,
      slug = page_basename,
      slug_field = "basename",
      extra_context = extra_context,
      template_object_name = "entry",
      template_name = settings.DEFAULT_TEMPLATE + "/page_detail.html"
    )

def app_page(request, template_name, blog_name = settings.DEFAULT_BLOG):
    style = get_style(request)
    
    response = HttpResponse()
    set_cookie(response, "style", style)

    blog = get_blog(request, blog_name)
    
    extra_context = {
      "style" : style,
      "blog_path" : "/" + blog_name + "/",
      "page_path" : "/" + blog_name + "/app/" + template_name + ".html",
      "blog_name" : blog_name,
      "blog" : blog,
    }
    
    return render_response(settings.DEFAULT_TEMPLATE + "/app/" + template_name + ".html", extra_context, response = response)
