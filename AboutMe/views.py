from django.shortcuts import render
from django.http import JsonResponse
from .models import Person, Skill, Education, Experience, Certification, Visitor
from .forms import VisitorForm

from django.core.mail import send_mail
from django.conf import settings

def home(request):
    context = {
        'person'    :   Person.objects.filter(name='Aditya Vasudeva').first(),
        'skill'     :   Skill.objects.filter(person_id__name='Aditya Vasudeva'),
        'edu'       :   Education.objects.filter(person_id__name='Aditya Vasudeva').order_by('-edu_dur'),
        'exp'       :   Experience.objects.filter(person_id__name='Aditya Vasudeva').order_by('-exp_dur'),
        'cert'      :   Certification.objects.all()
    }
    return render(request, 'AboutMe/index.html', context)

def submit_form(request):
    if request.method == 'POST':        
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()

            send_mail(
    		    subject="Someone got in touch!",
    		    message=request.POST['name'] + " with email id " + request.POST['email'] + " and Linkedin handle " + request.POST['linkedinh'] + " wanted to contact you!",
    		    from_email=settings.EMAIL_HOST_USER,
    		    recipient_list=[settings.EMAIL_HOST_USER])

            return JsonResponse({'message': 'Success'}, status=200)
        else:
            print(form.errors)
            return JsonResponse({'message': 'Form is not valid','errors':form.errors}, status=400)
    else:
        form = VisitorForm()
    return render(request, 'index.html', {'form': form})
    