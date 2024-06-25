from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import Usersform
from django.contrib.auth.models import User, auth 
from django.urls import reverse
from service.models import Signup,Register_quiz
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings


def loginPage(request):
    j = ''

    if request.method == "POST":
        if 'name1' in request.POST and 'email1' in request.POST and 'pass1' in request.POST:
            name1 = request.POST.get('name1')
            email1 = request.POST.get('email1')
            pass1 = request.POST.get('pass1')

            data = Signup(name1=name1, email1=email1, pass1=pass1)
            data.save()
            j = 'Data Inserted'

        elif 'email' in request.POST and 'pass_' in request.POST:
            email = request.POST.get('email')
            pass_ = request.POST.get('pass_')
            user = auth.authenticate(email=email, password=pass_)
            if request.user.is_authenticated:
                auth.login(request, user)
                return redirect('Home')
            

    return render(request, 'index_asmr.html', {'j': j})


def register(request):
    
    
    
    if request.method == "POST":
        fname=request.POST.get('fname')
        gender=request.POST.get('gender')
        birthday=request.POST.get('birthday')
        
        fname2=request.POST.get('fname2')
        gender2=request.POST.get('gender2')
        birthday2=request.POST.get('birthday2')
        
        fname3=request.POST.get('fname3')
        gender3=request.POST.get('gender3')
        birthday3=request.POST.get('birthday3')
        
        Collage=request.POST.get('Collage')
        Contact_no=request.POST.get('Contact_no')
        
        data=Register_quiz(fname=fname,gender=gender,birthday=birthday,fname2=fname2,gender2=gender2,birthday2=birthday2,fname3=fname3,gender3=gender3,birthday3=birthday3,Collage=Collage,Contact_no=Contact_no)
        data.save()
    
    
    
    return render(request,"index.html")
# def register_about(request):
    
#     try:
#         if request.method =="POST":
            
def about_us(request):
    
    return render(request,"about.html")

def service_quiz(request):
    subject = 'Testing mail'
    message = 'here is the message'
    from_email = 'django@mailtrap.club'
    recipient_list = ['quazifaraz508@gmail.com'] 

    send_mail(subject, message, from_email, recipient_list)
    return render (request,'services.html')

