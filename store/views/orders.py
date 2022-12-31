from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer
from django.views import View
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class OrderView(View):

   @method_decorator(auth_middleware)
   def get(self,request):
        customer = request.session.get('customer')
        orders= Order.get_orders_by_customer(customer)
        print(orders)
        orders = orders.reverse() # for showing last order in 1st 
        return render(request,'order.html',{'orders':orders})     