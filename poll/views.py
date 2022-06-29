from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
# Create your views here.
from django.contrib.auth.models import Group
from .models import Question, Choice
from .forms import ChoiceForm


def savollar(request):
    # bu yerda Question modelidagi barcha objectlar olinadi
    savollar = Question.objects.all()
    return render(
        request, 'questions/savollar.html', {'savollar': savollar})


def savol_detail(request, id):
    # bu yerda Question modelidan id si parametirklari kelayotgan
    # id ga teng bolgan object oliniadi
    savol = get_object_or_404(Question, id = id)
    return render(request, 'questions/savol.html', {'savol': savol})


def check_answer(request, variant_id):
    #bu yerda Choice modelidan id si parametirklari kelayotgan
    #variant_id ga teng bolgan object oliniadi
    javob = get_object_or_404(Choice, id=variant_id)
    correct = javob.is_correct
    return render(request, 'questions/checked.html', {'correct': correct})

def create_question(request):
    if request.method == "POST":
       question = request.POST.get('question') 
       Question.objects.create(question=question)
       return redirect("poll:savollar")
    return render(request, 'questions/create_question.html') 


# ===================================
def groups_add(request):
    if request.method == "POST":
       name = request.POST.get('name') 
       Group.objects.create(name=name)
       return redirect("poll:groups")
    return render(request, 'accounts/groups_add.html')

def group(request):
    groups = Group.objects.all()
    return render(request, 'accounts/groups.html', {'groups': groups})

def remove_group(request, id):
    group = get_object_or_404(Group, id=id)
    name = group.name
    group.delete()
    messages.add_message(request, level=messages.WARNING, message=f"Guruh [ {name} ] muvoffaqiyatli o'chirildi!")
    return redirect("poll:groups")


def edit_group(request, id):
    group = get_object_or_404(Group, id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        group.name = name
        group.save()
        messages.add_message(request, level=messages.SUCCESS, message=f"Guruh [ {name} ] muvoffaqiyatli o'zgartirildi!")
        return redirect("poll:groups")


def create_choice(request):
    form = ChoiceForm()
    if request.method == "POST":
        form = ChoiceForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("poll:savollar")
    return render(request, 'questions/create_choice.html', {"form": form})                