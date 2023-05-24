from django.shortcuts import render, redirect
import requests
import json
from .models import DishRestaurantMenuEntry


def start_view(request):
    return render(request, 'RMS/start_page.html')


def orders_view(request):
    return render(request, 'RMS/orders.html')

def tables_view(request):
    return render(request, 'RMS/table_booking.html')


def add_order_view(request):
    response = requests.get('http://localhost:8000/api/restaurant/menu')
    data = response.json()

    return render(request, 'RMS/add_order.html', {'data': data})


def menu_view(request):
    response = requests.get('http://localhost:8000/api/restaurant/menu')
    data = response.json()

    category1 = []  # Starter
    category2 = []  # Main course
    category3 = []  # Soup
    category4 = []  # Salad
    category5 = []  # Dessert

    for item in data:
        stage = item['stage']
        if stage == DishRestaurantMenuEntry.DishStage.STARTER:
            category1.append(item)
        elif stage == DishRestaurantMenuEntry.DishStage.MAIN_COURSE:
            category2.append(item)
        elif stage == DishRestaurantMenuEntry.DishStage.SOUP:
            category3.append(item)
        elif stage == DishRestaurantMenuEntry.DishStage.SALAD:
            category4.append(item)
        elif stage == DishRestaurantMenuEntry.DishStage.DESSERT:
            category5.append(item)

    return render(request, 'RMS/menu.html', {
        'category1': category1,
        'category2': category2,
        'category3': category3,
        'category4': category4,
        'category5': category5
    })


def dish_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        stage = request.POST.get('stage')
        weight = request.POST.get('weight')

        payload = {
            'name': name,
            'price': price,
            'stage': stage,
            'weight': weight
        }

        response = requests.post('http://localhost:8000/api/restaurant/menu', data=payload)

        if response.status_code == 201:
            return redirect('menu')

        else:

            return redirect('dish-form')
    else:
        return render(request, 'RMS/dish_form.html')




