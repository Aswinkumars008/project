from django.contrib import admin

from .models import Contact,Category,Product
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Product)