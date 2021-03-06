from django.db import models
from django.contrib.auth.models import User

class Customers(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=False)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name
    @property
    def imagURL(self):
        try:
            if self.image != '':
                url = self.image
            else:
                url = 'placeholder.png'
        except:
            url = 'placeholder.png'
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100,null=True)

    @property
    def get_card_total(self):
        order_item = self.orderitem_set.all()
        total_price = sum([order_i.get_total for order_i in order_item])
        return total_price
    @property
    def get_card_item(self):
        order_item = self.orderitem_set.all()
        total_item = sum([order_i.qunatity for order_i in order_item])
        return total_item

    @property
    def shipping(self):
        shipping = False
        orderitem = self.orderitem_set.all()
        for i in orderitem:
            if i.product.digital == False:
                shipping = True
        return shipping

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    qunatity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        return self.product.price * self.qunatity

    def __str__(self):
        return str(self.product.name)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customers,on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=500,null=False)
    city = models.CharField(max_length=500,null=False)
    state = models.CharField(max_length=500,null=False)
    zipcode = models.CharField(max_length=500,null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

# Create your models here.
