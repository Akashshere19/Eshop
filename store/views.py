from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
# Create your views here.
def index(request):
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
    return render(request,'index.html',data)

  
def signup(request): 
    if request.method == 'GET':
        print(request.method) # showing types of request 
        return render(request,'signup.html')
       
    else:
        postData = request.POST
        first_name = postData.get('first_Name')
        last_name = postData.get('last_Name')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        error_msg = None
        if (not first_name):
            error_msg = 'first Name is Requiered..!'
        elif first_name:
            if len(first_name) < 4:
                error_msg = 'first Name must be 4 character..!'
        elif not phone:
            error_msg = "phone no must..!"

        # print(first_name,last_name,phone,email,password)
        if not error_msg :
                     customer = Customer(first_name=first_name,last_name=last_name,
                                phone=phone,email=email,
                                password=password)
                     customer.register()
                     return HttpResponse('account Create')
        else:

                return render(request,'signup.html',{'error':error_msg})