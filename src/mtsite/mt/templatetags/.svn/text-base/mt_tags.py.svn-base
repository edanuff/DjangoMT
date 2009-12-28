import re
import os
from datetime import datetime

from django import template
from django.conf import settings

from mtsite.mt.models import Blog
from mtsite.mt.models import Entry
from mtsite.mt.models import Comment

MONTH_NAMES = ('', 'January', 'Feburary', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December')

register = template.Library()

re_tag_var_name = re.compile("(.*)\s*as\s+(\w*)\s*\Z")
re_tag_params = re.compile('((\w*)="([^"]*)"\s*)')

#
# Django doesn't impose a standard convention for tag parameters
#
# For consistency with classic MT Tags, all tags used by this module use the
# convention of name="value" for tag parameters
#
# {% mt_entries lastn="15" %}
#
# Similar to other Django tags, tags which set a template context variable
# can specify this via an 'as' clause after the tag name/value parameters:
#
# {% mt_entries lastn="15" as entries %}
#
# This is optional, all tags have a default variable they set if this is
# not specified
#

def get_tag_params(contents, var_name):
    
    params = dict()  
    params["var_name"] = var_name
    
    match = re_tag_var_name.match(contents)
    if match:
      token = match.group(1)
      params["var_name"] = match.group(2)

    iterator = re_tag_params.finditer(contents)
    for match in iterator:
      params[match.group(2)] = match.group(3)
      
    return params
  
def get_value(context, key):
    try:
      return context[key]
    except KeyError:
      pass
    return None

def get_blog(context):
    
    blog = get_value(context, "blog")
    if blog:
      return blog
    
    blog_name = get_value(context, "blog_name")    
    if not blog_name:
      return None

    try:
      blog = Blog.objects.get(site_path__iendswith = blog_name)
    except Blog.DoesNotExist: 
      return None
    
    context["blog"] = blog
     
    return blog

'''
 Tag: mt_blog
 Parameters: none
 Description: Gets the blog object for the current context
'''

class BlogNode(template.Node):
    def __init__(self, params):
        self.params = params

    def render(self, context):

        blog = get_blog(context)
        if not blog:
          return ''
            
        return ''

@register.tag
def mt_blog(parser, token):
    params = get_tag_params(token.contents, "mt_blog")      
    return ContextNode(params)

'''
 Tag: mt_entries
 Parameters: entry, author, category, tag, lastn, limit
 Description: Gets the entries list for the current blog
'''

class EntriesNode(template.Node):
    def __init__(self, params):
        self.params = params

    def render(self, context):

        blog = get_blog(context)
        if not blog:
          return ''
    
        entries = blog.entries.filter(class_field="entry")

        if "author" in self.params:
          entries = entries.filter(author__name = self.params["author"])
        
        if "category" in self.params:
          entries = entries.filter(categories__label = self.params["category"])
        
        if "tag" in self.params:
          entries = entries.filter(tags__name = self.params["tag"])
        
        entries.order_by("-created_on")
        
        if "lastn" in self.params:
          entries = entries[:int(self.params["lastn"])]        
        elif "limit" in self.params:
          entries = entries[:int(self.params["limit"])]
        else:
          entries = entries[:15]
        
        context[self.params["var_name"]] = entries
        
        return ''

@register.tag
def mt_entries(parser, token):
    params = get_tag_params(token.contents, "entries")      
    return EntriesNode(params)
  
'''
 Tag: mt_top_level_categories
 Parameters: none
 Description: Gets the top level categories for the current blog
'''

class TopLevelCategoriesNode(template.Node):
    def __init__(self, params):
        self.params = params

    def render(self, context):

        blog = get_blog(context)
        if not blog:
          return ''
    
        blog_categories = blog.categories.filter(class_field = "category")
        blog_categories = blog_categories.filter(parent = 0)
        
        context[self.params["var_name"]] = blog_categories
        
        return ''

@register.tag
def mt_top_level_categories(parser, token):
    params = get_tag_params(token.contents, "blog_categories")      
    return TopLevelCategoriesNode(params)

'''
 Tag: mt_pages
 Parameters: none
 Description: Gets the pages for the current blog
'''

class PagesNode(template.Node):
    def __init__(self, params):
        self.params = params

    def render(self, context):

        blog = get_blog(context)
        if not blog:
          return ''
    
        blog_pages = blog.entries.filter(class_field = "page")
        blog_pages = blog_pages.order_by("title")
        blog_pages = blog_pages.values("id", "title", "basename")
        
        context[self.params["var_name"]] = blog_pages
        
        return ''

@register.tag
def mt_pages(parser, token):
    params = get_tag_params(token.contents, "blog_pages")      
    return PagesNode(params)

'''
 Tag: mt_comments
 Parameters: author, visible, lastn, limit
 Description: Get the comments list for the current entry
'''

class CommentsNode(template.Node):
    def __init__(self, params):
        self.params = params

    def render(self, context):

        blog = get_blog(context)
        if not blog:
          return ''
    
        if not context["entry"]:
          return ''
        
        entry = context["entry"]
        
        comments = entry.comments.all()

        if "author" in self.params:
          comments = comments.filter(author__name = self.params["author"])
        
        if "visible" in self.params:
          comments = comments.filter(visible = self.params["visible"])
        
        comments.order_by("-created_on")
        
        if "lastn" in self.params:
          comments = comments[:int(self.params["lastn"])]        
        elif "limit" in self.params:
          comments = comments[:int(self.params["limit"])]
        
        context[self.params["var_name"]] = comments
        
        return ''

@register.tag
def mt_comments(parser, token):
    params = get_tag_params(token.contents, "comments")      
    return CommentsNode(params)
  
'''
 Tag: mt_entry_categories
 Parameters: label
 Description: Gets the categories for the current entry
'''

class EntryCategoriesNode(template.Node):
    def __init__(self, params):
        self.params = params

    def render(self, context):

        blog = get_blog(context)
        if not blog:
          return ''
    
        if not context["entry"]:
          return ''
        
        entry = context["entry"]
        
        entry_categories = entry.categories.all()

        entry_categories.order_by("label")
        
        context[self.params["var_name"]] = entry_categories
        
        return ''

@register.tag
def mt_entry_categories(parser, token):
    params = get_tag_params(token.contents, "categories")      
    return EntryCategoriesNode(params)
  
'''
 Tag: mt_archive_list
 Parameters: type, lastn, sort_order
 Description: Gets the archives for the current blog
'''

class ArchiveListNode(template.Node):
    def __init__(self, params):
        self.params = params

    def render(self, context):

        blog = get_blog(context)
        if not blog:
          return ''
    
        if "type" in self.params:
          pass
        
        if "lastn" in self.params:
          pass
        
        if "sort_order" in self.params:
          pass  
       
        archive_data = []
        
        count = {}
        mcount = {}
        entries = blog.entries.filter(class_field="entry")
        entries = entries.values("created_on")
        
        for entry in entries:
            year = entry["created_on"].year
            month = entry["created_on"].month
            
            if year not in count:
                count[year] = 1
                mcount[year] = {}
            else:
                count[year] += 1
                
            if month not in mcount[year]:
                mcount[year][month] = 1
            else:
                mcount[year][month] += 1
                
        for year in sorted(count.iterkeys(), reverse=True):
            archive_data.append({'isyear': True,
                                 'year': year, 
                                 'count': count[year],})
            
            for month in sorted(mcount[year].iterkeys(), reverse=True):
                archive_data.append({'isyear': False,
                                     'year': year, 
                                     'yearmonth': '%d/%02d' % (year, month),
                                     'monthname': MONTH_NAMES[month], 
                                     'count': mcount[year][month],})
        
        context[self.params["var_name"]] = archive_data
        
        return ''

@register.tag
def mt_archive_list(parser, token):
    params = get_tag_params(token.contents, "archives")      
    return ArchiveListNode(params)
  
'''
 Tag: mt_style_list
 Parameters: none
 Description: Gets the styles for the current blog
'''

class StyleListNode(template.Node):
    def __init__(self, params):
        self.params = params

    def render(self, context):
    
        styles = os.listdir(os.path.join(settings.PROJECT_PATH, 'styles'))
        styles.sort()
        
        context[self.params["var_name"]] = styles
        
        return ''

@register.tag
def mt_style_list(parser, token):
    params = get_tag_params(token.contents, "styles")      
    return StyleListNode(params)
  
