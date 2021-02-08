from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout_user,name="logout"),
]

# for login,register(sign up),logout view we can have urlpattern as login/,register/,logout/ and views can also have any name but for logout view especially we should choose a different name as there is already a logout view , so choose name like logout_user,etc.