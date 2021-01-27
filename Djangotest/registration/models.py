from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=24, null=True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    description = models.TextField(User,default='Hello')

    def __str__(self):
        return f'{self.user.username} Profile'

class Product(models.Model):
    name = models.CharField(max_length=250, null=True)
    price = models.FloatField()
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    description = models.CharField(max_length=250, null=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True,blank=False)
    eyw_transactionref = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = True
        orderitems = self.orderitem_set.all()

        return shipping
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    order_transactionref = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    @property
    def get_items(self):
        item = self.product.name
        return item

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    postcode = models.CharField(max_length=10, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Diary(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=24, null=True)
    description = models.TextField(User, default='Hello')

    def __str__(self):
        return str(self.id)

class DiaryItem(models.Model):
    name = models.CharField(max_length=24, null=True)
    diary = models.ForeignKey(Diary, on_delete=models.SET_NULL, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)