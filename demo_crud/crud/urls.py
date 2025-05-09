from django.urls import path
import _mysql_connector

from crud import views

urlpatterns = [
        path('', views.index, name='index'),
        path('customer_edit/<int:id>', views.customer_edit, name='customer_edit'),
        path('customer_delete/<int:id>', views.customer_delete, name='customer_delete'),

          ]