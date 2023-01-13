from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'date', 'in_stock']
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'price', 'date', 'in_stock')
    list_editable = ('price', 'in_stock')
    list_filter = ('title', 'price', 'date', 'in_stock')


admin.site.register(Item, ItemAdmin)
