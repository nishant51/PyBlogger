from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import *
from .forms import *  
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def homepage(request):                 #reading the data 
    data=Blog.objects.all()
    return render(request,'index.html',{'data':data})

def about(request):
    return render (request,'about.html')



def create(request):
   form=updateform()
   if request.method=='POST':
        form=updateform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
         form = updateform()
   return render(request, 'create.html', {'form': form})  

""" 
def create(request):                    #creating the data
    if request.method == 'POST':
        form = Blog(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            pc= Blog(
                title = cd['title'],
                body = cd['body'],
                author =cd['author']
            )
            pc.save()  # save the form data to the database
            return redirect('home')
    else:
        form = post()
 
    return render(request, 'create.html', {'form': form})
 """

def editblog(request,pk):                                 #editing the data
    op=Blog.objects.get(id=pk)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=op)
        if form.is_valid():
            form.save()
            return redirect('home')            # Redirect to a success page or do something else
    else:
        form = EditForm(instance=op)
    return render(request, 'edit.html', {'form': form,'pk': pk})

def delete(request,pk):
    ab=Blog.objects.get(id=pk)
    ab.delete()
    return redirect('home')
 
def readmore(request,pk):
    blog=get_object_or_404(Blog,id=pk)
    return render(request,'detail.html',{'blog':blog})

def loginpage(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user =authenticate(request,username=username,password=password)

        if user is not None:
                login(request, user)
                return redirect('home')
        else:
             messages.info(request,'Provided credential doesnot match our database')


    context = {}
    return render(request,'login.html',context)



def register(request):
    form = Createuserform()
    if request.method == 'POST':
        form = Createuserform(request.POST)
        if form.is_valid:
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created sucessfully' + user)
            return redirect('login')

    context = {'form':form}
    return render(request,'register.html',context)


def logoutpage(request):
    logout(request)
    return redirect('home')