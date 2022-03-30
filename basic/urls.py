from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('blog',views.blog,name='blog'),
    path('booking',views.booking,name='booking'),
    path('contact',views.contact,name='contact'),
    path('feature',views.feature,name='feature'),
    path('menu',views.menu,name='menu'),
    path('single',views.single,name='single'),
    path('team',views.team,name='team'),
    path('addFood',views.addFood,name='addFood'),
    # path('addFoodDB',views.addFoodDB,name='addFoodDB'),
    path('registration',views.register,name='register'),
    path('login',views.login_,name='login'),
    path('order',views.order_,name='order')
]