from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password # for hide password grom user and also from admin

from django.views import View

class Signup(View):
     def get(self,request): 
                print(request.method) # showing types of request 
                return render(request,'signup.html')
     def post(self,request):
                postData = request.POST
                first_name = postData.get('first_Name')
                last_name = postData.get('last_Name')
                phone = postData.get('phone')
                email = postData.get('email')
                password = postData.get('password')
                value = {
                    'first_name':first_name,
                    'last_name':last_name,
                    'phone':phone,
                    'email':email,
                }
                print('value::',value)
                error_msg = None
                customer = Customer(first_name=first_name,last_name=last_name,
                                        phone=phone,email=email,
                                        password=password)
                error_msg = self.validateCustomer(customer)                        
                if (not first_name):
                    error_msg = 'first Name is Requiered..!'
                elif (not last_name):
                    
                    error_msg = 'last Name must be required..!'
                elif (not phone):
                    error_msg = "phone no must..!"
                elif len(phone)<10:
                    error_msg = "phone no must be 10 digit..!"
                # print(first_name,last_name,phone,email,password)

                elif customer.isExists():
                    error_msg = "Email  Address already Registered..!"

                if not error_msg :
                            customer.password=make_password(customer.password)
                            print(customer.password)
                            customer.register()
                            return redirect('homepage') # for avoid http error
                else:
                            
                    data = {
                        'error':error_msg,
                        'values':value
                    }
                    return render(request,'signup.html',data)

     def validateCustomer(self,customer):
                error_msg =None
                if (not customer.first_name):
                    error_msg = 'first Name is Requiered..!'
                elif (not customer.last_name):
                    
                    error_msg = 'last Name must be 4 character..!'
                elif (not customer.phone):
                    error_msg = "phone no must..!"
                elif len(customer.phone)<10:
                    error_msg = "phone no must be 10 digit..!"
                # print(first_name,last_name,phone,email,password)

                elif customer.isExists():
                    error_msg = "Email  Address already Registered..!"
                return error_msg