from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from .forms import ItemForm
from .models import Item
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    # template = loader.get_template('index.html')
    # user = request.user
    # context={
    #     'user':user,
    # }
    # return HttpResponse(template.render(context,request))
    return render(request, 'index.html')

def items(request):
    items = Item.objects.all().values()
    template = loader.get_template('items.html')
    context = {
        'items': items,
    }
    return HttpResponse(template.render(context,request))

def item(request,id):
    item = Item.objects.get(id=id)
    template = loader.get_template('item.html')
    context = {
        'item': item,
    }
    return HttpResponse(template.render(context,request))

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('items')
    
    else:
        form = ItemForm()

    template = loader.get_template('add_item.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context,request))

def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect('items')