from django.shortcuts import render
from store.models.product import Product
from store.models.category import Category

from django.views import View

# print(make_password('1234'))
# a=check_password('1234','pbkdf2_sha256$390000$LGr7UmRBmrzT8cVRAMmuFG$QzcDP2bbAcSGpTZwJorcZeg4F2T30zYk/fkfiKg+MDU=')
# print(a)

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



