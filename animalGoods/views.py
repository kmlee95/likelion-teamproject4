from django.shortcuts import render, get_object_or_404, redirect
from .models import Goods, Comment
from django.utils import timezone

# Create your views here.


def animalGoods(request):
    goodss = Goods.objects
    postComment = Comment.objects
    return render(request, 'animalGoods.html', {'goodss': goodss, 'comments': postComment, 'user': request.user})


def detail(request, goods_id):  # detail은 두개의 인자를 받는다

    goods_detail = get_object_or_404(Goods, pk=goods_id)
    return render(request, 'detail.html', {'goods_detail': goods_detail})


def write(request):
    if request.user.is_authenticated:
        return render(request, 'write.html')
    else:
        return redirect('signin')


def create(request):
    goods = Goods()
    goods.title = request.POST['title']
    goods.image = request.FILES['image']
    goods.body = request.POST['body']
    goods.save()
    return redirect('/animalGoods/')


def comment(request, ):
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment = Comment()
            comment.comment = request.POST['text']
            comment.pup_date = timezone.datetime.now()
            comment.author = request.user
            comment.save()
            return redirect('/animalGoods/')
        else:
            return redirect('signin')
