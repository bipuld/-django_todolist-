from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from userapp.forms import CustomForm
# Create your views here.
def signup(request):
    if request.method == 'POST':
        signup_form=CustomForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
        messages.success(request, "Your account has been sucessfully created.")
        return redirect('task')
    else:
        signup_form=CustomForm()
    context={
            'form': signup_form
        }
    return render(request, 'signup.html', context)

