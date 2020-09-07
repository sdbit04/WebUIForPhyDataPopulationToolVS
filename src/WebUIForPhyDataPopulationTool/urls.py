"""WebUIForPhyDataPopulationTool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from .views import index
# from product.views import daughter, myself, wife, home
# from customers.views import retail_customer_details, create_retail_customer, edit_retail_customer, \
    # delete_retail_customer, retail_customers_list

urlpatterns = [
    path('welcome/', index, name='index'),
    path('customers-', include('customers.urls')),
    path('family/', include('family.urls'), name='family_welcome'),
    path('admin/', admin.site.urls),
    path('', index)
]
