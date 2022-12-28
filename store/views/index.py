from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View
# print(make_password('1234'))
# a=check_password('1234','pbkdf2_sha256$390000$LGr7UmRBmrzT8cVRAMmuFG$QzcDP2bbAcSGpTZwJorcZeg4F2T30zYk/fkfiKg+MDU=')
# print(a)

# Create your views here.
class Index(View):
    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        #print('product:',product)
        if cart:
            quantity =cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:    
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1       
        else:
            cart = {}
            cart[product] = 1
        request.session['cart']= cart 
        print('cart items:',request.session['cart'])       
       # print('product_id:',product)
        return redirect('homepage')
        
    def get(self,request):
        #request.session.get('cart').clear()
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        prds  = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        
        if categoryID:
            prds = Product.get_all_products_by_categoryid(categoryID)
        else: 
            prds = Product.get_all_products()
        data ={}
        data['products'] = prds
        data['catagories'] = categories
        
        #print(ctg)
        #print(prds)
        # print(data)
        print('email:',request.session.get('customer_email'))
        return render(request,'index.html',data)



