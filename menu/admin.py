from django.contrib import admin
from .models import Category, MenuItem
from ordered_model.admin import OrderedModelAdmin

# Register your models here.
class MenuItemAdmin(OrderedModelAdmin):
    # ...
    list_display = ('id', 'title', 'description', 'price', 'active', 'move_up_down_links')

class CategoryAdmin(OrderedModelAdmin):
    # ...
    list_display = ('id', 'category', 'active', 'move_up_down_links')

admin.site.register(Category, CategoryAdmin)
admin.site.register(MenuItem, MenuItemAdmin)