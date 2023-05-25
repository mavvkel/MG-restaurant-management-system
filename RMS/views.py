from django.shortcuts import render


def start_view(request):
    return render(request, 'RMS/start_page.html')


def orders_view(request):
    return render(request, 'RMS/orders_page.html')


