from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import *
from django.http import JsonResponse
import json
import datetime
from .filters import ProductFilter
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form})

def store(request):
    if 'i' in request.GET:
        i = request.GET['i']
        products = Product.objects.filter(name=i)
        myFilter = ProductFilter(request.GET, queryset=products)
        products = myFilter.qs
        context = {'products': products, 'title': 'Store'}
    else:
        products = Product.objects.all()
        myFilter = ProductFilter(request.GET, queryset=products)
        products = myFilter.qs
        context = {'products': products,'title': 'Store','myFilter':myFilter}
    return render(request, 'users/store.html', context)

def Checkout(request):
    print("checkout")
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(Profile=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        order = {'get_cart_total':0,}
        items = []
    context = {'items': items, 'order': order}
    return render(request, 'users/checkout.html', context)

def cart(request):
    print("cart")
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(Profile=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        order = {'get_cart_total': 0, }
        items = []
    context = {'items':items,'title': 'Cart','order': order}
    return render(request, 'users/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(Profile=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items':items}
    return render(request, 'users/cart.html', context)
def updateItem(request):

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print(action)
    print(productId)
    

    customer = request.user.profile
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(Profile=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('item added',safe=False)

def processOrder(request):
    print("process")
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(Profile=customer, complete=False)
        order.complete = True
        order.save()

        ShippingAddress.objects.create(
                customer =customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
        )
        ShippingAddress.save()
    return JsonResponse('payment recieved', safe=False)

def ProductDetailView(request,pk):
    item = get_object_or_404(Product,id=pk)
    context = {'item':item,'title': item}
    return render(request, 'users/product.html',context)

@login_required()
def profile(request):
    return render(request, 'users/profile.html')