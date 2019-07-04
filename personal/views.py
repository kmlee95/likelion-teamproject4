from django.shortcuts import render

# Create your views here.


def personal(request):
    return render(request, 'personal.html')
