from django.conf import settings

def blog(request):
  
  '''
  Eventually, this should scan the request path to capture the variables
  the same way the urlpatterns are matched
  '''

  style = settings.DEFAULT_STYLE
  blog_name = settings.DEFAULT_BLOG
  
  return {
    "style" : style,
    "blog_path" : "/" + blog_name + "/",
    "page_path" : "/" + blog_name + "/",
    "blog_name" : blog_name,
  }
