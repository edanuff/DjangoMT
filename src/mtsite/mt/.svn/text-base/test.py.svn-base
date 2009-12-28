from mt.models import Tag 
from mt.models import Entry

def test_entries():
  entries = Entry.objects.all()
  for entry in entries:
    print entry
    print entry.tags.all()
    
def test_entries_by_tag():
  entries = Entry.objects.filter(tags__name="apple")    
  for entry in entries:
    print entry

def test_entries_from_tag():
  tags = Tag.objects.filter(name="apple")
  for tag in tags:
    entries = tag.entries.all()    
    for entry in entries:
      print entry
