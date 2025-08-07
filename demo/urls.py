"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include as inc
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inc('myappp.urls')), # This mean stay to main domain --> https://mydomain.com --> Hello World!!!
    path('homePages/',inc('myappp.urls')) # if "homePages" doesnt have this: -> '/, it will lock on this page and Django doesnt let to Browser to get next pages of homePages 
    #like this: -> without '/': mydomain.com/homePages/blog (It wont work!!!) ,,,, With this '/' -> mydomain.com/homePages/blog (I will Work!!!!)
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

