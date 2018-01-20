from django.contrib import admin
from .models import WikiItem, WikiCraftProduct, WikiCraftProductType
# Register your models here.

admin.site.register(WikiItem)
admin.site.register(WikiCraftProductType)
admin.site.register(WikiCraftProduct)
