"""
URL configuration for week12 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from userauth.views import login_view, register_view, index_view, logout_view

#self code 
from userauth.views import home_view,test_view,forgetpwd_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="register"),
    path('index/', index_view, name="index"),
    
    
    
    #self
    path('', home_view, name='home'),
    path('test/', test_view, name='test'),
    path('forgetpwd/', forgetpwd_view, name='forgetpwd'),
    
]
