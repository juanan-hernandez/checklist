from django.http import HttpResponse, HttpResponseRedirect

from .forms import ItemForm
from .models import ChecklistItem
from django.template import loader
from django.shortcuts import redirect

def index(request):
    return HttpResponse("Hello, world. You're at the checklist index.")

def item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        description = form.data['description']
        new_item = ChecklistItem(description=description)
        new_item.save()
        return HttpResponseRedirect("/checklist/")
    else:
        pass

def items(request):
    all_items = ChecklistItem.objects.all()
    template = loader.get_template('checklist/index.html')
    # output = ', '.join([q.description for q in all_items])
    context = {
        'checklist_items': all_items,
    }
    return HttpResponse(template.render(context, request))
