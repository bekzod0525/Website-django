import re
from django.shortcuts import get_object_or_404, redirect, render


from .models import New
from .forms import NewForm, NewFormMine

def news_list(request):
    news = New.objects.all().order_by('-created')# queryset
    # context dictionary bu templetega berib yuboriladigan uzgaruvchilar tuplami
    context = {'news': news}
    return render(request, 'new/news_list.html', context)
    

def news_detail(request, id):
    new = get_object_or_404(New, id=id)# queryset
    return render(request, 'new/news_detail.html', {'new': new})
    

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
