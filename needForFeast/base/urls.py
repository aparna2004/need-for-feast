from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.loginPage,name = 'login'),
    path('logout/',views.logoutUser,name = 'logout'),
    path('register_customer/',views.registerCustomer,name = 'register_customer'),
    path('register_owner/',views.registerOwner,name = 'register_owner'),
    path('register_deliverer/',views.registerDeliverer,name = 'register_deliverer'),
    path('role/',views.selectRole, name='role'),
    path("", views.home, name="home"),
    path("order/", views.order, name="order"),
]
