from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('booking',views.booking,name='booking'),
    path('contact',views.contact,name='contact'),
    path('menu',views.menu,name='menu'),
    path('addCart',views.cart,name='cart'),
    path('addFood',views.addFood,name='addFood'),
    # path('addFoodDB',views.addFoodDB,name='addFoodDB'),
    path('registration',views.register,name='register'),
    path('login',views.login_,name='login'),
    path('cartView',views.cartView,name='cartView'),
    path('inc',views.plus,name='pl'),
    path('dec',views.minus,name='mn'),
    path('emptyCart',views.emptyCart,name='emptyCart'),
    path('checkout',views.checkout,name='checkout'),
    path('profile',views.profile,name='profile'),
    path('updateProfile',views.updateProfile,name='uprofile'),
    path('viewOrders',views.viewOrder,name='vorder'),
    path('adminHome_',views.adminHome_,name='aHome'),
    path('updateitem',views.updateItem,name='iupdate'),
    path('updatefood',views.updateFood,name='fupdate'),
    path('removeitem',views.removeItem,name='iremove'),
    path('orderDone',views.orderDone,name='orderDone'),
    path('order',views.order_,name='order')
]

urlspatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)