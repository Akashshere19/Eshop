from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password  # for hide password grom user and also from admin
from django.views import View


class Login(View):
    def get(self,request):
        return render(request,'login.html') 
    def post(self,request):
        email = request.POST.get('email') 
        password = request.POST.get('password')
        customer = Customer.getCustomer_by_email(email)
        error_msg= None
        if customer:
            flag= check_password(password,customer.password)
            if flag :
               return redirect('homepage')
            else:
                error_msg = 'Email and Password invalid..!'

            
        else:
            error_msg = 'Email and password required'
        print('name :',customer)
        print('email & pw:',email,password)
        return render(request,'login.html',{'error':error_msg}) 