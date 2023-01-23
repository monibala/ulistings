from django.contrib import admin

from home.models import contact_info, order

# Register your models here.
admin.site.register(order)
# admin.site.register(location)
admin.site.register(contact_info)