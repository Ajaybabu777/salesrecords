from django.urls import path
from . import views

urlpatterns = [
    path('sales/', views.sales_record_list, name='sales_record_list'),
    path('sales/add/', views.add_sales_record, name='add_sales_record'),
    path('sales/edit/<int:pk>/', views.edit_sales_record, name='edit_sales_record'),
    path('sales/download/', views.download_sales_records, name='download_sales_records'),
]