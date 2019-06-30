from django.shortcuts import render

# Create your views here.


def animalGoods(request):
    return render(request, 'animalGoods.html')
