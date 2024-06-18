from django.shortcuts import render,redirect,get_object_or_404
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
    


# ============================   Editing Post ======================
def edit(request,id):
    post=get_object_or_404(BlogPost,id=id)

    if request.method=='POST':
        form=CreatePost(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_post')
        else:
            return render(request,'edit_post',{'frm':form})
    
    return render(request,'edit.html',{'form':CreatePost(instance=post),'id':id})




# ============================  Deleting Post ======================

def delete(request,id):
    post=get_object_or_404(BlogPost,id=id)
    post.delete()
    return redirect('blog_post')