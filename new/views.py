from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render


from .models import New, Like, Dislike
from .forms import NewForm, NewFormMine, CommentForm

def news_list(request):
    news = New.objects.all().order_by('-created')# queryset
    # context dictionary bu templetega berib yuboriladigan uzgaruvchilar tuplami
    context = {'news': news}
    return render(request, 'new/news_list.html', context)
    

def news_detail(request, id):
    new = get_object_or_404(New, id=id)# queryset
    form = CommentForm()
    if request.method == 'POST':
        #commit formaga postga kelyotgan malumotlarni
        #berib validatsiyadan otkazadi
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = new
            if request.user.is_authenticated:
                comment.author = request.user
            comment.save()
        return redirect('new:detail', id=id)
    return render(request, 'new/news_detail.html', {'new': new, "form": form})
    

def create(request):
    form = NewForm
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save()
            return redirect('new:list')
    return render(request, 'new/create.html', {'form': form })    



def remove(request, id):
    new = get_object_or_404(New, id=id)
    new.delete()
    return redirect("new:list")    


def my_news(request):
    news = New.objects.filter(author=request.user).order_by('-created')
    return render(request, 'new/my_news.html', {'news': news})    


def my_create(request):
    form = NewFormMine
    if request.method == 'POST':
        form = NewFormMine(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.author = request.user
            new.save()
            return redirect('new:my_news')
    return render(request, 'new/create.html', {'form': form })    

def my_update(request, id):
    new = get_object_or_404(New, id=id)
    form = NewFormMine(instance=new)
    if request.method == 'POST':
        form = NewFormMine(request.POST, request.FILES, instance=new) 
        if form.is_valid():
            new.save()
            return redirect('new:my_news')
    return render(request, 'new/create.html', {'form': form })    

def my_detail(request, id):
    new = get_object_or_404(New, id=id)

    return render(request, 'new/my_detail.html', {"new": new})


def Like(request, id):
    new = get_object_or_404(New, id=id)
    if request.user.is_authenticated:
        if new.likes.filter(user=request.user).exists():
            new.likes.get(user=request.user).delete()
            return JsonResponse(
                {
                'success': True,
                'message': "Siz reaksiyangizni qaytarib oldingiz!",
                'likes': new.likes.count()
                }
            )
        Like.objects.create(user=request.user, post=new)
        return JsonResponse(
                {
                'success': True,
                'message': "Sizga yoqqan postlar safiga qo'shildi!",
                'likes': new.likes.count()
                }
            )
    return JsonResponse(
                {
                'success': False,
                'message': "Postga reaksiya bildirish uchun iltimos ro'yhatdan o'ting!",
                }
            )        



def Dislike(request, id):
    new = get_object_or_404(New, id=id)
    if request.user.is_authenticated:
        if new.dislikes.filter(user=request.user).exists():
            new.dislikes.get(user=request.user).delete()
            return JsonResponse(
                {
                'success': True,
                'message': "Siz reaksiyangizni qaytarib oldingiz!",
                'dislikes': new.dislikes.count()
                }
            )
        Dislike.objects.create(user=request.user, post=new)
        return JsonResponse(
                {
                'success': True,
                'message': "Sizga yoqmagan postlar safiga qo'shildi!",
                'dislikes': new.dislikes.count()
                }
            )
    return JsonResponse(
                {
                'success': False,
                'message': "Postga reaksiya bildirish uchun iltimos ro'yhatdan o'ting!",
                }
            )
