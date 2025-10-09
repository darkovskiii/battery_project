from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from .forms import ItemForm
from .models import Item
from django.contrib.auth import authenticate
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid

# Create your views here.
def index(request):
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

def buy_item(request,id):
    item = Item.objects.get(id=id)

    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': item.price,
        'item_name': item.name,
        'no_shipping': '2',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': 'https://{}{}'.format(host,reverse("paypal-ipn")),
        'return_url': 'https://{}{}'.format(host,reverse("payment_success")),
        'cancel_return': 'https://{}{}'.format(host,reverse("payment_failed")),
    }

    paypal_form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'paypal_form.html',{"paypal_form":paypal_form})


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

def payment_success(request):
    return render(request, "payment_success.html")

def payment_failed(request):
    return render(request, "payment_failed.html")