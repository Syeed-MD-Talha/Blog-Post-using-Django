from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

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