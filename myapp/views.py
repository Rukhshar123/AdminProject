from typing import re

from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.sessions.models import Session

def login(request):
    if request.session.has_key('IS_LOGIN'):
        return redirect('home')

    if request.POST:
        email=request.POST['email']
        password=request.POST['password']
        # select * from user  where email='' and password=''
        count=User.objects.filter(email=email,password=password).count()
        if count>0:
            request.session['IS_LOGIN']=True
            admin_email = "v@gmail.com"
            if admin_email == email :
               # request.session['user_id'] =User.objects.values('id').filter(email=email,password=password)[0]['id']
                request.session['user_id'] = User.objects.values('id')[0]['id']
                return redirect('admin_home')
            else :
                return redirect('home')
            #return HttpResponse("Login done")
        else:
            messages.error(request,'Wrong Id Password')
            #return HttpResponse("wrong id pass")
            #return redirect('login')

    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')


"""def register_user(request):
    if request.POST:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        obj=User(username=username,email=email,password=password)
        obj.save()

        return HttpResponse(username+" "+email+" "+password)

    return HttpResponse("Register Done")"""

def register_user(request):
    if request.POST:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        obj=User(username=username,email=email,password=password)
        obj.save()
        messages.success(request,'register done')
        return redirect('login')

def admin_home(request):
    if request.session.has_key('IS_LOGIN'):
       fatchData = Blog.objects.all()
       print(fatchData)
       return render(request,'admin_home.html',{'data':fatchData})
    return redirect('login')

def home(request):
    if request.session.has_key('IS_LOGIN'):
       fatchData = Blog.objects.all()
       print(fatchData)
       return render(request,'home.html',{'data':fatchData})
    return redirect('login')


def logout(request):
    del request.session['IS_LOGIN']
    return redirect('login')


def createPost(request):
    if request.POST:
        name=request.POST['name']
        title=request.POST['title']
        description=request.POST['description']
        image=request.POST['image']
        user_id=request.session['user_id']

        obj=Blog(name=name,
                 description=description,
                 title=title,
                 image=image)
        obj.userid_id = user_id

        obj.save()
        messages.success(request,'your post upload done')
        return redirect('home')

    return render(request,'createpost.html')



def readmore(request,id):
    if request.POST:
        message=request.POST['message']
        user_id=request.POST['user_id']
        post_id=id

        query= Comment(message=message)
        query.post_id_id=post_id
        query.user_id_id=user_id
        query.save()
        #return HttpResponse("cmnt done")
    data = Blog.objects.get(id=id)
    comment = Comment.objects.all().filter(post_id=id)
    return render(request,'readmore.html', {'data':data,'comment':comment})



