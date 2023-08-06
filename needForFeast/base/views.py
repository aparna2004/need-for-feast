from django.shortcuts import render
from django.http import HttpResponse
from .models import Items, Order
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,"base/home.html")

def order(request):
    items = Items.objects.all()
    context= {'items' : items}
    if request.method == 'POST':
        item_list = request.POST.getlist('item_list')
        qty_list = request.POST.getlist('quantity_list')
        print("Items :", item_list)
        qty_list = [x for x in qty_list if x!='']
        ordered_items = []
        for key in item_list:
            ordered_items.append(Items.objects.get(id=key))
        for i in ordered_items:
            print(i.name)
        if len(item_list)!=len(qty_list):
            messages.error("Invalid selection. Try again")
            
        return HttpResponse("Thank you for ordering")
    return render(request, 'base/order.html',context=context)