from django.shortcuts import render
from .forms import RegisterForm #현재 경로의 forms.py의 RegisterForm class를 import


#회원가입
def register(request):
    if request.method == 'POST':    
        user_form = RegisterForm(request.POST)
        print(user_form)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user'})
    else:
        user_form = RegisterForm()
        print("a")

    return render(request, 'registration/register.html',{'form':user_form})