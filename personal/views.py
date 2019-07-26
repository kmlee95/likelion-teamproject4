from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Personal
from django.core.paginator import Paginator


def personal(request):
    personals = Personal.objects
    personal_list = Personal.objects.all()
    paginator = Paginator(personal_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'personal.html', {
        'personals': personals,
        'posts': posts,
        'user': request.user
    })


def delete(request, personal_id):
    personal = get_object_or_404(Personal, pk=personal_id)
    personal.delete()
    return redirect('/')


def detail(request, personal_id):
    detail = get_object_or_404(Personal, pk=personal_id)
    return render(request, 'detail.html', {'personal': detail, 'personal_id': str(personal_id)})


def writePerson(request):
    return render(request, 'writePerson.html')


def createPerson(request):
    photo = Personal()
    photo.title = request.POST['title']
    photo.image = request.FILES['image']
    photo.pub_date = timezone.datetime.now()
    photo.body = request.POST['body']
    photo.author = request.user
    photo.save()
    return redirect('/personal')
