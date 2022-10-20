from django.http import HttpResponse
from .models import ChecklistItem
from django.template import loader

def index(request):
    return HttpResponse("Hello, world. You're at the checklist index.")

def items(request):
    all_items = ChecklistItem.objects.all()
    template = loader.get_template('checklist/index.html')
    # output = ', '.join([q.description for q in all_items])
    context = {
        'checklist_items': all_items,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse(output)