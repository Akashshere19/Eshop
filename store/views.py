from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
# Create your views here.
def index(request):

    prds = Product.get_all_products()
    ctg = Category.get_all_categories()
    data ={}
    data['products'] = prds
    data['catagories'] = ctg 
    #print(ctg)
    #print(prds)
    # print(data)
    return render(request,'index.html',data)

  