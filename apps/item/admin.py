from django.contrib import admin

from apps.item.models import Item, ItemCategories, CustomItem

admin.site.register(Item)
admin.site.register(ItemCategories)
admin.site.register(CustomItem)
