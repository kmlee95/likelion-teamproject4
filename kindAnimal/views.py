from django.shortcuts import render


# Create your views here.
def kindAnimal(request):
    return render(request, 'kindAnimal.html')
