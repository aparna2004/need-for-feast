from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.loginPage,name = 'login'),
    path('logout/',views.logoutUser,name = 'logout'),
    path('register/',views.registerUser,name = 'register'),

    path("", views.home, name="home"),
    path("order/", views.order, name="order"),
]
