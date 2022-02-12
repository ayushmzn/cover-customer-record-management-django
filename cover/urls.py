"""cover URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from coverapp import views
from django.conf.urls import url
from django.urls import path
urlpatterns = [
    url('^$',views.login_page),
    path('login_done',views.login_done),
    path('try_again',views.try_again),
    path('home', views.home),
    path('add_new_customer', views.add_new_customer),
    path('add_new_customer_done', views.add_new_customer_done),
    path('search_customer', views.search_customer),
    path('searched_customer', views.searched_customer),
    path('view_all_customers', views.view_all_customers),
    path('Entry_to_send_goods', views.Entry_to_send_goods),
    path('entry_save', views.entry_save),
    path('Entry_for_deposit_money', views.Entry_for_deposit_money),
    path('add_credit_money', views.add_credit_money),
    path('view_customer_details', views.view_customer_details),
    path('Entry_to_send_goods_inside_view_details', views.Entry_to_send_goods_inside_view_details),
    path('entry_save_inside_view_details', views.entry_save_inside_view_details),
    path('Entry_for_deposit_money_inside_details', views.Entry_for_deposit_money_inside_details),
    path('add_credit_money_inside_view', views.add_credit_money_inside_view),
    path('edit_details', views.edit_details),
    path('update_details', views.update_details),
    path('view_customer_details_edited', views.view_customer_details_edited),
    path('deletedetails', views.deletedetails),
path('detele_details_confirm', views.detele_details_confirm),
path('edit_costomer', views.edit_costomer),
path('update_customer', views.update_customer),
path('delete_customer', views.delete_customer),
path('detele_customer_confirm', views.detele_customer_confirm),
path('userlogout', views.userlogout),
    path('admin/', admin.site.urls),
]
