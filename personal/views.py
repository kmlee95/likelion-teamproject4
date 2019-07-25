from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Personal
from django.core.paginator import Paginator

def personal(request):
    personals = Personal.objects
    personal_list = Personal.objects.all()
    paginator = Paginator(personal_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'personal.html', {'personals':personals, 'posts':posts})

def detail(request, personal_id):
    detail = get_object_or_404(Personal, pk = personal_id)
    return render(request, 'detail.html', {'personal' : detail})

def write(request):
    return render(request, 'write.html')

def create(request):
    photo = Personal()
    photo.title = request.POST['title']
    photo.image = request.FILES['image'] 
    photo.pub_date = timezone.datetime.now()
    photo.body = request.POST['body']
    photo.save()
    return redirect('/personal')

