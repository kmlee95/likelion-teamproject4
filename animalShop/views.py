from django.shortcuts import render

# Create your views here.


def animalShop(request):
    return render(request, 'animalShop.html')
