from django import forms

class Usersform(forms.Form):
    num1=forms.CharField()
    num2=forms.CharField()
    
class Form_login(forms.Form):
    name_id= forms.CharField()
    email_id=forms.EmailField()
    pass_id=forms.PasswordInput()
