from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

# Create your views here.
def store(request):

    if request.user.is_authenticated:
        customer = request.user.customers
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_card_item
    else:
        order = {'get_card_total': 0, 'get_card_item': 0, 'shipping': False}
        items = []
        cartItems = order['get_card_item']

    products = Product.objects.all()
    context = {"products":products, "cartItems":cartItems}

    return render(request,'store/store.html',context)
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customers
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_card_item
    else:
        order = {'get_card_total':0,'get_card_item':0, 'shipping': False}
        items = []
        cartItems = order['get_card_item']
    context = {'items': items, 'order' : order, 'cartItems' : cartItems}
    return render(request,'store/cart.html',context)
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customers
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_card_item
    else:
        order = {'get_card_total': 0, 'get_card_item': 0, 'shipping': False}
        items = []
        cartItems = order['get_card_item']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request,'store/checkout.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productID = data['producrId']
    action = data['action']
    print('Product ID: ',productID)
    print('Action: ',action)

    customer = request.user.customers
    product = Product.objects.get(id = productID)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    Order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'ad d':
        Order_item.qunatity = (Order_item.qunatity + 1)
    elif action == 'remove':
        Order_item.qunatity = (Order_item.qunatity - 1)
    Order_item.save()
    if Order_item.qunatity <=0:
        Order_item.delete()
    z = sum(1,2)

    return JsonResponse("It was added", safe=False)

def process_order():
    return JsonResponse("Payment Done")