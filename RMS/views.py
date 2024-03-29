from django.shortcuts import render, redirect
import requests
import json
from .models import DishRestaurantMenuEntry


def start_view(request):
    return render(request, 'RMS/start_page.html')


def orders_view(request):
    return render(request, 'RMS/orders.html')


def tables_view(request):
    response = requests.get('http://localhost:8000/api/restaurant/table')
    table_data = response.json()

    table_category_window = []
    table_category_kitchen = []
    table_category_garden = []
    table_category_bar = []
    table_category_isolated = []

    for item in table_data:
        properties = item['properties']
        if properties == 1:
            table_category_window.append(item)
        elif properties == 2:
            table_category_kitchen.append(item)
        elif properties == 3:
            table_category_garden.append(item)
        elif properties == 4:
            table_category_bar.append(item)
        elif properties == 5:
            table_category_isolated.append(item)

    return render(request, 'RMS/table_booking.html', {
        'table_category_window': table_category_window,
        'table_category_kitchen': table_category_kitchen,
        'table_category_garden': table_category_garden,
        'table_category_bar': table_category_bar,
        'table_category_isolated': table_category_isolated
    })


def add_order_view(request):
    response = requests.get('http://localhost:8000/api/restaurant/menu')
    data = response.json()

    return render(request, 'RMS/add_order.html', {'data': data})


def menu_view(request):
    response = requests.get('http://localhost:8000/api/restaurant/menu')
    data = response.json()

    dish_category_starter = []  # Starter
    dish_category_main_course = []  # Main course
    dish_category_soup = []  # Soup
    dish_category_salad = []  # Salad
    dish_category_dessert = []  # Dessert

    drink_category_alcoholic = []
    drink_category_non_alcoholic = []

    for item in data:
        resourcetype = item['resourcetype']
        if resourcetype == 'DishRestaurantMenuEntry':
            stage = item['stage']
            if stage == 1:
                dish_category_starter.append(item)
            elif stage == 2:
                dish_category_main_course.append(item)
            elif stage == 3:
                dish_category_soup.append(item)
            elif stage == 4:
                dish_category_salad.append(item)
            elif stage == 5:
                dish_category_dessert.append(item)
        elif resourcetype == 'DrinkRestaurantMenuEntry':
            contains_alcohol = item.get('contains_alcohol', False)
            if contains_alcohol:
                drink_category_alcoholic.append(item)
            else:
                drink_category_non_alcoholic.append(item)

    return render(request, 'RMS/menu.html', {
        'dish_category_starter': dish_category_starter,
        'dish_category_main_course': dish_category_main_course,
        'dish_category_soup': dish_category_soup,
        'dish_category_salad': dish_category_salad,
        'dish_category_dessert': dish_category_dessert,
        'drink_category_alcoholic': drink_category_alcoholic,
        'drink_category_non_alcoholic': drink_category_non_alcoholic
    })




def dish_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        stage = int(request.POST.get('stage'))
        weight = request.POST.get('weight')

        payload = {
            'name': name,
            'price': price,
            'resourcetype': 'DishRestaurantMenuEntry'
        }

        if stage in [1, 2, 3, 4, 5]:
            payload['stage'] = stage
            payload['weight'] = weight

        response = requests.post('http://localhost:8000/api/restaurant/menu', json=payload)

        if response.status_code == 201:
            return redirect('menu')
        else:
            return redirect('dish-form')
    else:
        return render(request, 'RMS/dish_form.html')


def table_form_view(request):
    if request.method == 'POST':
        capacity = request.POST.get('capacity')
        properties = int(request.POST.get('properties'))

        payload = {
            'capacity': capacity,
        }

        if properties in [1, 2, 3, 4, 5]:
            payload['properties'] = properties

        response = requests.post('http://localhost:8000/api/restaurant/table', json=payload)

        if response.status_code == 201:
            return redirect('tables')
        else:
            return redirect('table-form')
    else:
        return render(request, 'RMS/table_form.html')


def drink_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        contains_alcohol = bool(request.POST.get('contains_alcohol'))
        volume = request.POST.get('volume')

        payload = {
            'name': name,
            'price': price,
            'contains_alcohol': contains_alcohol,
            'volume': volume,
            'resourcetype': 'DrinkRestaurantMenuEntry'
        }

        response = requests.post('http://localhost:8000/api/restaurant/menu', json=payload)

        if response.status_code == 201:
            return redirect('menu')
        else:
            return redirect('drink-form')
    else:
        return render(request, 'RMS/drink_form.html')


def workers_view(request):
    # this will not work b/c of the need for authentication
    response = requests.get('https://rms.restaurant.pool.kot.tools/api/restaurant/worker')
    data = response.json()
    workers = []
    workers = data

    return render(request, 'RMS/workers.html', {
        'workers': workers
    })




