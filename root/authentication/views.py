from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm,PasswordUpdateForm,CustomUserChangeForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page(request):
     return redirect(request,'home.html')



def sign_up(request):
    if request.method=='GET':
         print("=================== GET ==============")
         form=RegisterForm()
         return render(request,'registration.html',{'form':form})
    else:
         frm=RegisterForm(request.POST)
         print("=================== PoSt ==============")
         if frm.is_valid():
                print("!!!!!!!!!!!!!Sucessfully register!!!!!!!!!!!!!!!!!")
                frm.save()
                return redirect('home_page')
         form=RegisterForm
         return render(request,'registration.html',{'form':form})


   
def log_in(request):
     if request.method=='POST':
          info=LoginForm(request.POST)
          if info.is_valid():
               print("============ Post method =============")
               username=info.cleaned_data['username']
               password=info.cleaned_data['password']
               user=authenticate(request,username=username,password=password)
               if user:
                    login(request,user)
                    messages.success(request,'Successfully login!!!')
                    return redirect('home_page')

          print("ERROR !!!!!!!!!!")
          messages.error(request,'Invalid username or password!!!!')
          return render(request,'login.html',{'form':info})
     
     else:
          frm=LoginForm()
          print("=============== GET method ==========")
          return render(request,'login.html',{'form':frm})
     


def log_out(request):
     logout(request)
     return redirect('login_page')




@login_required
def update_profile(request):
    if request.method == 'POST':
        if 'update_profile' in request.POST:
              form=CustomUserChangeForm(request.POST,instance=request.user)
              if form.is_valid():
                  form.save()
                  return redirect('home_page')
              else:
                messages.error(request, 'Please correct the errors below.')

        if 'change_password' in request.POST:
              password_form = PasswordUpdateForm(request.user, request.POST)
              if password_form.is_valid():
                    password_form.save()
                    return redirect('home_page')
              else:
                messages.error(request, 'Please correct the errors below.')
        
    else:
        form=CustomUserChangeForm(instance=request.user)
        password_form = PasswordUpdateForm(request.user)

    context = {'form':form,'password_form': password_form}
    return render(request, 'profile_update.html', context)

