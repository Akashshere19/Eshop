from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer
from django.views import View


class Checkout(View):
    def post(self,request):
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            customer = request.session.get('customer')
            cart = request.session.get('cart')
            products = Product.get_product_by_id(list(cart.keys()))

            #print(address,phone,customer,products)
            
            for product in products:
                #print(cart.get(str(product.id)))
                order = Order(customer = Customer(id=customer),product = product,
                               address = address,phone=phone,
                               price = product.price,
                               quantity = cart.get(str(product.id)))
                order.save()               
                #print(order.placeOrder())  
            request.session['cart'] = {}             
            return redirect('cart')