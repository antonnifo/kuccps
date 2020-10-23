from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import ProgrammeChoice,Programme, Institution
                                                                         

# @login_required
# def dashboard(request):

#     student = get_object_or_404(Student,
#                             id=request.user.id
#                            )
    
#     return render(request,
#                         'account/dashboard.html',
#                         {'section': 'dashboard',
#                          'student':student
#                         })

def programme_choices(request):
    return render(request,
                    'account/programmes_choices.html',
                    {'section': 'programmes',
                        
                        'choices': ProgrammeChoice.objects.all(),
                    })

def institutions(request):   
    return render(request,
                    'account/institutions.html',
                    {
                        'section': 'schools',
                        'schools': Institution.objects.all(),

                    })                    

def programmes(request):
    return render(request,
                    'account/programmes.html',
                    {
                        'section': 'pro',
                        'programmes': Programme.objects.all(),

                    })  