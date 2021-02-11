from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,DiaryAdditionForm
from .models import *
from django.http import JsonResponse, FileResponse, Http404,HttpResponse
import json
from django.views.generic import ListView, DetailView, CreateView,UpdateView
import datetime
from .filters import ProductFilter,ProfileFilter
from django.db.models import Case, Value, When,CharField,ImageField
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
        if i != "":
            products = Product.objects.filter(name=i)
            myFilter = ProductFilter(request.GET, queryset=products)
            products = myFilter.qs
            context = {'products': products, 'title': 'Store'}
        else:
            products = Product.objects.all()
            myFilter = ProductFilter(request.GET, queryset=products)
            products = myFilter.qs
            context = {'products': products, 'title': 'Store', 'myFilter': myFilter}
    else:
        products = Product.objects.all()
        myFilter = ProductFilter(request.GET, queryset=products)
        products = myFilter.qs
        context = {'products': products,'title': 'Store','myFilter':myFilter}
    return render(request, 'store/store.html', context)

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
    return render(request, 'store/checkout.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(Profile=customer, complete=False)
        print(order)
        items = order.orderitem_set.all()
        print(items)
    else:
        order = {'get_cart_total': 0, }
        items = []
    context = {'items':items,'title': 'Cart','order': order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(Profile=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items':items}
    return render(request, 'store/cart.html', context)
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

    products3 = Product.objects.annotate(
        order=Case(
            When(id=pk), then=Value('1'),
            default=Value('0'),
            output_field=ImageField(),
        )
    ).order_by('order')
    print(products3)
    item = get_object_or_404(Product,id=pk)
    if pk == 1:
            print(Product.objects.count())
            ProductCount = Product.objects.count()
            backwardId = pk+ProductCount-1
            forwardId = pk + 1
            print(forwardId, backwardId,"pk 0")
            context = {'item': item, 'title': item, "products": products3, "idforward": forwardId,
                       "idbackwards": backwardId}
    elif pk == Product.objects.count():
            print(Product.objects.count())
            ProductCount = Product.objects.count()
            backwardId = pk - 1
            forwardId = pk - ProductCount+1
            print(forwardId, backwardId,"pkMax")
            context = {'item': item, 'title': item, "products": products3, "idforward": forwardId,
                       "idbackwards": backwardId}
    else:
            forwardId = pk+1
            backwardId = pk-1
            print(forwardId,backwardId)
            context = {'item':item,'title': item,"products":products3,"idforward":forwardId,"idbackwards":backwardId}
    return render(request, 'store/product.html',context)

def ViewProfile(request,username):
        profile = Profile.objects.filter(name=username)[0]
        print(profile)
        context = {'profile':profile}
        print(context)
        return render(request, 'users/user_profile.html',context)
        #follow querey sets ^^ this will sort it
def pdf_view(request):
    image_data = open('Djangotest\media\documents\Laurie_Humphries-Cable_CV.pdf', 'rb').read()
    return HttpResponse(image_data, content_type='application/pdf')
@login_required()
def profile(request):
    return render(request, 'users/profile.html')

def diaryrequest(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        diaryItem = Diary.objects.filter(Profile=customer)
        #diaryItem = diary.diaryitem_set.all()
        DiaryTasks = DiaryItem.objects.filter(Profile=customer)
        print(DiaryTasks)
    else:
        diary = {'get_cart_total': 0, }
        diaryItem = []
        DiaryTasks = []
    context = {'diarys':diaryItem,'diaryitems':DiaryTasks}
    return render(request, 'diary/diary.html', context)

class DiaryCreateView(CreateView):
    model = Diary

    fields = ['name','description']

    def form_valid(self, form):
        form.instance.Profile = self.request.user.profile
        return super().form_valid(form)

class DiaryItemCreateView(CreateView):
    template_name = 'registration/diary_form.html'
    form_class = DiaryAdditionForm
    def form_valid(self, form):
        form.instance.Profile = self.request.user.profile
        return super().form_valid(form)
    def get_form_kwargs(self):
        kwargs = super(DiaryItemCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user.profile
        return kwargs
