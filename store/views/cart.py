from django.shortcuts import render,redirect
from store.models.product import Product
from django.contrib.auth.hashers import check_password  # for hide password grom user and also from admin
from django.views import View


class Cart(View):

    def get(self,request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_product_by_id(ids)
        print(products)
       # print(list(request.session.get('cart').keys()))
        return render(request,'cart.html',{'products':products}) 
  