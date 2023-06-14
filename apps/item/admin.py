from django.contrib import admin

from apps.item.models import Item, ItemCategory, CustomItem

admin.site.register(Item)
admin.site.register(ItemCategory)
admin.site.register(CustomItem)
