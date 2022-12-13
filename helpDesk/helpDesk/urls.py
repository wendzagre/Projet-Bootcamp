"""helpDesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include,path
import authentication.views
from  gestion import views






urlpatterns = [
   path('admin/', admin.site.urls),
    path('Agent/',include('Agent.urls'),name='agent'),
    path('gestion/', include('gestion.urls'),name='ticket'), #Inclure l'urls.py de l'application gestion
    path('',authentication.views.login_page,name='login') ,
    path('logout/',authentication.views.logout_user,name='logout') ,
    path('demande/',views.Demande,name='demande') ,
    path('faq/',views.FAQ,name='faq') ,
    path('agent/',views.Lagent,name='create-agent') ,
    path('signup/',authentication.views.signup_page,name='signup'),
    








]
