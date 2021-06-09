from django.shortcuts import render,redirect
from django.http import HttpResponse
from project.forms import UserForm,TeacherForm,VideoForm,Doubt1Form
from project.models import user,teacher,videoentry,student,doubt
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
# Create your views here.
def view1(request):
    a=user.objects.all()
    return render(request,'new 1.html',{'q':a})
def view2(request):
    a=student.objects.all()
    return render(request,'new 2.html',{'q':a})
def view3(request):
    a=teacher.objects.all()
    return render(request,'new 3.html',{'q':a})
def view4(request):
    a=videoentry.objects.all()
    return render(request,'new 4.html',{'q':a})
def view5(request):
    a=doubt.objects.all()
    return render(request,'new 5.html',{'q':a})
def view6(request):
    a=teacher.objects.all()
    return render(request,'new 6.html',{'q':a})
def index(request):
    return render(request,'index.html')
def index1(request):
    return render(request,'index1.html')
def index2(request):
    return render(request,'index2.html')
def reg(request):
    return render(request,'register.html')
def log(request):
    return render(request,'login.html')
def c1(request):
    a=teacher.objects.all()
    return render(request,'show3.html',{'q':a})
def c3(request):
    return render(request,'courseenter.html')
def c4(request):
    return render(request,'l1.html')
def c6(request):
    return render(request,'l3.html')
def c7(request):
    return render(request,'login2.html')
def c8(request):
    return render(request,'doubtenter.html')
def c9(request):
    if request.method=="POST":
        su_name=request.POST['su_name']
        email=request.POST['email']
        u=doubt.objects.filter(su_name=su_name,email=email)
        return render(request,'show7.html',{'q':u})   
def d1(request):
    if request.method=="POST":
        f=Doubt1Form(request.POST)
        if f.is_valid():
            f.save()
            messages.info(request,'doubt Registered sucessfully')
            return render(request,'vie3.html')
    else:
        f=DoubtForm()
    return redirect('../c3')
def check(request):
    if request.method=="POST":
        u_name=request.POST['u_name']
        pwd=request.POST['pwd']
        u=user.objects.get(u_name=u_name,pwd=pwd)
        return render(request,'show.html',{'q':u}) 
def coursefind(request):
    if request.method=="POST":
        su_name=request.POST['su_name']
        email=request.POST['email']
        u=student.objects.filter(su_name=su_name,email=email)
        return render(request,'show4.html',{'q':u})   
def insert(request):
    if request.method=="POST":
        u_name=request.POST['u_name']
        name=request.POST['u_name']
        email=request.POST['email']
        pwd=request.POST['pwd']
        roles=request.POST['roles']
        ph=request.POST['ph']
        try:
            u=user.objects.get(u_name=u_name)
        except:
            u=None
        if u is not None:
            messages.info(request,'user name is already taken')
            return render(request,'register.html')
        try:
            u=user.objects.get(email=email)
        except:
            u=None
        if u is not None:
            messages.info(request,'emailid is already registered')
            return render(request,'login.html')
        f=user(u_name=u_name,email=email,name=name,pwd=pwd,ph=ph,roles=roles)
        try:
            f.save()
            return  redirect('../project/log')
        except:
            pass
    else:
        f=UserForm()
    return render(request,'register.html')
def view(request,u_name,coursecode):
     u=videoentry.objects.filter(u_name=u_name,coursecode=coursecode)
     return render(request,'show5.html',{'q':u})
def videoenter(request):
    if request.method=="POST":
        f=VideoForm(data=request.POST,files=request.FILES)
        try:
            f.save()
            return  redirect('../c4')
        except:
            pass
    else:
        f=CourseForm()
    return redirect('../c3')
def studentreg(request):
    if request.method=="POST":
        tu_name=request.POST['tu_name']
        su_name=request.POST['su_name']
        coursecode=request.POST['coursecode']
        name=request.POST['name']
        email=request.POST['email']
        try:
            u=student.objects.get(tu_name=tu_name,su_name=su_name,name=name,email=email,coursecode=coursecode)
        except:
            u=None
        if u is not None:
            messages.info(request,'you can not register to same course twice')
        else:
            u=student(tu_name=tu_name,su_name=su_name,name=name,email=email,coursecode=coursecode)
            try:
                u.save()
                messages.info(request,'registered successfully')
                return render(request,'l2.html')
            except:
                pass
    return render(request,'l2.html') 
def d2(request,tu_name,coursecode):
     u=doubt.objects.filter(tu_name=tu_name,coursecode=coursecode)
     return render(request,'show8.html',{'q':u})
def db(request,u_name,coursecode,caption):
     u=videoentry.objects.get(u_name=u_name,coursecode=coursecode,caption=caption)
     return render(request,'vie3.html',{'q':u})
def watch(request,u_name,coursecode,caption):
     u=videoentry.objects.get(u_name=u_name,coursecode=coursecode,caption=caption)
     return render(request,'vie2.html',{'q':u})    
def register(request,u_name,coursecode):
     u=teacher.objects.get(u_name=u_name,coursecode=coursecode)
     return render(request,'l2.html',{'q':u})
def c2(request):
    if request.method=="POST":
        f=TeacherForm(request.POST)
        if f.is_valid():
            try:
                f.save()
                return  redirect('../project/index2')
            except:
                pass
    else:
        f=TeacherForm()
    return render(request,'index1.html')

def sr(request,u_name,coursecode):
     u=student.objects.filter(tu_name=u_name,coursecode=coursecode)
     return render(request,'show6.html',{'q':u})
def delete(request,u_name,coursecode):
     u=videoentry.objects.filter(u_name=u_name,coursecode=coursecode)
     return render(request,'show2.html',{'q':u})
def deleteentry(request,u_name,coursecode,caption):
     u=videoentry.objects.get(u_name=u_name,coursecode=coursecode,caption=caption)
     u.delete();
     a=videoentry.objects.filter(u_name=u_name,coursecode=coursecode)
     return render(request,'show2.html',{'q':a})
def deldoubt(request,tu_name,coursecode,caption,su_name):
     u=doubt.objects.get(tu_name=tu_name,coursecode=coursecode,caption=caption,su_name=su_name)
     u.delete();
     return render(request,'index1.html')
def c5(request):
    if request.method=='POST':
        u_name=request.POST['u_name']
        u=teacher.objects.filter(u_name=u_name)
        if u is not None:
            return render(request,'show1.html',{'q':u})
        else:
            messages.info(request,'there is no course you created previously')
            return redirect('../project/c4')
    else:
        return render(request,'index2.html')  
def course(request,u_name,coursecode):
    u=teacher.objects.get(u_name=u_name,coursecode=coursecode)
    return render(request,'video.html',{'q':u})
def vie(request):
    a=student.objects.all()
    return render(request,'show.html',{'q':a})
def vie2(request):
    a=videoentry.objects.all()
    return render(request,'vie2.html',{'q':a})
def enter(request):
    if request.method=='POST':
        u_name=request.POST['u_name']
        pwd=request.POST['pwd']
        u=user.objects.filter(u_name=u_name,pwd=pwd)
        if u is not None:
            for i in u:
                if i.roles=='student':
                    return render(request,'index1.html')
            return render(request,'index2.html')
        else:
            messages.info(request,'error')
            return redirect('../project/log')
    else:
        return render(request,'register.html')