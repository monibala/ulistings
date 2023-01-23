from django.contrib import admin

from Category.models import  Features, ListCategories, List,   MenuItems, bookedlist, reviews, wishitems

# Register your models here.
admin.site.register(ListCategories)
admin.site.register(List)
admin.site.register(wishitems)
admin.site.register(MenuItems)
admin.site.register(bookedlist)
admin.site.register(Features)
admin.site.register(reviews)
