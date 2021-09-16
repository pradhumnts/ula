from django.db.models.base import ModelBase
from django.shortcuts import render
from .models import Category, MenuItem

# Create your views here.
def index(request):
    return render(request, 'menu/index.html')
    
def menu(request):
    menu_items =  MenuItem.objects.filter(active=True)
    category = Category.objects.filter(active=True)
    context = {
        'menu_items': menu_items,
        'category': category
    }
    return render(request, 'menu/menu.html', context=context)

def add_item(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        print(category)
        MenuItem.objects.create(title=title, description=description, price=price, category=category)

    return render(request, 'menu/add_item.html')
