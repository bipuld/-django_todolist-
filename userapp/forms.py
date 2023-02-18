from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from phonenumber_field.formfields import PhoneNumberField
# from phonenumber_field.phonenumber import PhoneNumber

class CustomForm(UserCreationForm):   
    username = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    # phone=PhoneNumberField()  
    # sex_check=[
    #     ('M','male'),('F','female'),('O','other')
    # ] 
    # gender=forms.ChoiceField(choices=sex_check,widget=forms.RadioSelect())

   

    class Meta:
        model=User
        # fields=['firstname','lastname','username','email','password1','password2','phone']
        fields=['first_name','last_name','username','email','password1','password2']
    
