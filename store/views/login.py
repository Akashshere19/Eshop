
from django.shortcuts import render,redirect,HttpResponseRedirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password  # for hide password grom user and also from admin
from django.views import View


class Login(View):

    return_url = None


    def get(self,request):
        Login.return_url = request.GET.get('return_url')
        return render(request,'login.html') 
    def post(self,request):
        email = request.POST.get('email') 
        password = request.POST.get('password')
        customer = Customer.getCustomer_by_email(email)
        error_msg= None
        if customer:
            flag= check_password(password,customer.password)
            if flag :
                request.session['customer'] = customer.id
                #request.session['customer_email'] = customer.email
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                        Login.return_url = None
                        return redirect('homepage')
               
            else:
                error_msg = 'Email and Password invalid..!'

            
        else:
            error_msg = 'Email and password required'
        print('name :',customer)
        print('email & pw:',email,password)
        return render(request,'login.html',{'error':error_msg}) 


def logout(request):
    request.session.clear()
    return redirect('login')