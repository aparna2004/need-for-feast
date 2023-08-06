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
        qty_list = [x for x in qty_list if x!='' and x!='0']
        print(qty_list)
        amt=0
        # bill=[
        #     {'name': 0, 'price':0}, ...
        # ]
        if ( len(item_list)!=len(qty_list) ) :
            messages.error(request,"Invalid selection. Enter again")
            return render(request, 'base/order.html',context=context)
        
        bill=[]
        loop=0
        for key in item_list:
            record = Items.objects.get(id=key)
            bill_item=dict( )
            print(record.name,record.price,qty_list[loop])
            bill_item['name']=record.name
            bill_item['price']=int(record.price)
            bill_item['qty']=qty_list[loop]
            bill.append(bill_item)
            print(bill_item)
            loop+=1
            amt+=(record.price)
        
        if amt==0:
            messages.error(request,"No items have been chosen. Try again!")
            return render(request, 'base/order.html',context=context)
        
        order=Order.objects.create(amount=amt)
        order.items.add(*item_list)
        order.save()
        print(bill)
        return render(request, 'base/order_confirm.html',{'bill':bill,'amount':amt})
        
        return HttpResponse("Thank you for ordering")
    return render(request, 'base/order.html',context=context)