from django.contrib import admin
from coverapp.models import user_info,add_customer,customer_transections
admin.site.register(user_info)
admin.site.register(add_customer)
admin.site.register(customer_transections)
# Register your models here.
