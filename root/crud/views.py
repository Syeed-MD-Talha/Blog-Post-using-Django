from django.shortcuts import render,redirect
from .forms import CreatePost
from .models import BlogPost

# Create your views here.

def home(request):
    data=BlogPost.objects.all()
    return render(request,'crud.html',{'info':data})


def create(request):
    if request.method=='GET':
        print("................GET METHOD..........")
        frm=CreatePost()
        return render(request,'create.html',{'form':frm})
    
    else:
        print("----------POST METHOD---------")
        frm=CreatePost(request.POST,request.FILES)
        if frm.is_valid():
            print('------------- valid ????? ------------')
            frm.save()
            return redirect('blog_post')
        else:
            print('Form is not valid: ',frm.errors)
        return render(request,'create.html',{'form':frm})
    

