from django.contrib import admin
from models import Blog
from models import Entry

class EntryAdmin(admin.ModelAdmin):
    fields = ("title", "text", "created_on")
    list_display = ('title', 'created_on')
    list_filter = ('blog',)
    date_hierarchy = 'created_on'
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(EntryAdmin, self).formfield_for_dbfield(db_field, **kwargs) # Get the default field
        if db_field.name == "created_on": # Check if it's the one you want
            field.widget.attrs['readonly'] = "readonly" # Poke in the new 
        return field


class BlogAdmin(admin.ModelAdmin):
    fields = ('name', 'description')
    list_display = ('name',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Entry, EntryAdmin)


