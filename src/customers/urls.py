from django.contrib import admin
from django.urls import path
from .views import retail_customer_details, create_retail_customer, edit_retail_customer, \
    delete_retail_customer, retail_customers_list, customer_page

urlpatterns = [
    path('Retail/<int:id>/', retail_customer_details, name='retail_customer_details'),
    path('Home/', customer_page),
    path('CreateRetail/', create_retail_customer),
    path('Retailers/', retail_customers_list),
    path('EditRetail/<int:id>', edit_retail_customer),
    path('DeleteRetail/<int:id>', delete_retail_customer)   
]
