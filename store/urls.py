from django.contrib import admin
from django.urls import path
from .views import index,login,signup,cart,checkout,orders
from .views.login import logout
from .middlewares.auth import auth_middleware
urlpatterns = [
    path('',index.Index.as_view(),name='homepage'),
    path('signup',signup.Signup.as_view(),name='sign'),
    path('login',login.Login.as_view(),name='login'),
    path('logout',logout,name='logout'),
    path('cart',cart.Cart.as_view(),name='cart'),
    path('checkout',checkout.Checkout.as_view(),name='checkout'),
    path('orders',auth_middleware(orders.OrderView.as_view()),name='order'),

]
