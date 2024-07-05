from django.shortcuts import render
from django.http import JsonResponse
from .models import Person, Skill, Education, Experience, Certification, Visitor
from .forms import VisitorForm

def home(request):
    context = {
        'person'    :   Person.objects.filter(name='Aditya Vasudeva').first(),
        'skill'     :   Skill.objects.all(),
        'edu'       :   Education.objects.all(),
        'exp'       :   Experience.objects.all(),
        'cert'      :   Certification.objects.all()
    }
    return render(request, 'AboutMe/index.html', context)

def submit_form(request):
    if request.method == 'POST':        
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Success'}, status=200)
        else:
            print(form.errors)
            return JsonResponse({'message': 'Form is not valid','errors':form.errors}, status=400)
    else:
        form = VisitorForm()
    return render(request, 'index.html', {'form': form})
    