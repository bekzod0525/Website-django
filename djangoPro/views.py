from django.shortcuts import HttpResponse, render

# djangoni user modelini emport qildik
from django.contrib.auth.models import User, Group

from new.models import New
from extra.models import Carusel

def home(request):
    news = New.objects.all()[:3]
    carusels = Carusel.objects.all()
    return render(request, 'pages/home.html',{'news': news, 'carusels': carusels })


def users_view(request):
    users = User.objects.all()
    return render(request,  'accounts/users.html', {"users": users})


def groups_view(request):
    groups = Group.objects.all()
    return render(request,  'accounts/groups.html', {"groups": groups})    