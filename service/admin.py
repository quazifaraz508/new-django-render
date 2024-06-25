from django.contrib import admin
from service.models import Service,Signup,Register_quiz

class ServiceAdmin(admin.ModelAdmin):
    list_display=('sev_title','ser_dec')
    
admin.site.register(Service,ServiceAdmin)
# Register your models here.
class Signup_admin(admin.ModelAdmin):
    list_display=('name1','email1','pass1')
admin.site.register(Signup,Signup_admin)

class Register_admin(admin.ModelAdmin):
    list_display=('fname','gender','birthday','fname2','gender2','birthday2','fname3','gender3','birthday3','Collage','Contact_no')
admin.site.register(Register_quiz,Register_admin)


