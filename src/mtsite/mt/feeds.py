from django.contrib.syndication.feeds import Feed
from models import Blog
from models import Entry

class LatestEntriesForBlog(Feed):
    title_template = 'feeds/title.html'
    description_template = 'feeds/description.html'

    def get_object(self, bits):
        if len(bits) < 1:
            raise ObjectDoesNotExist
        self.blog_name = bits[0]
        self.blog = Blog.objects.get(site_path__iendswith = self.blog_name)  
        return self.blog   

    def title(self, obj):
        return obj.name

    def link(self, obj):
        return "/" + self.blog_name + "/index.html"

    def description(self, obj):
        return obj.description

    def item_link(self, obj):
        year = obj.created_on.year
        month = obj.created_on.month
        return "/" + self.blog_name + "/" + '%d/%02d' % (year, month) + "/" + obj.basename + ".html"

    def items(self, obj):
         return obj.entries.filter(class_field = "entry").order_by('-created_on')[:10]
