from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
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
    return render(request,'signup.html')