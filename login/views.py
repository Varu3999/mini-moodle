from django.shortcuts import render , get_object_or_404 , redirect ,render_to_response
from django.http import HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.views import generic
from django.views.generic import View
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.contrib import auth
from django.template.defaulttags import csrf_token
from django.contrib.auth.forms import UserCreationForm
from .models import user_type , teacher ,student, courses, sc , message
import datetime

from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    if request.user:
        logout(request)
    return render(request , 'login/login.html',{});

def loggedin(request):

    u = user_type.objects.filter(user = request.user)
    if u[0].is_teach == True:
        t = teacher.objects.filter(user = request.user)
        if not t:
            print("hi")
            p = teacher()
            p.user = request.user
            p.noc = 0
            p.save()
            type = "teacher"
        else:
            p = t[0]
        myc = courses.objects.filter(teacher = p)
        return render(request, 'login/teacher.html',{"user" : request.user, "mycourses": myc})
    else:
        t = teacher.objects.filter(user=request.user)
        if not t:
            print("hi")
            p = student()
            p.user = request.user
            p.noc = 0
            p.cg = 0
            p.save()
        else:
            p = t[0]
        s = student.objects.filter(user = request.user)

        myc = sc.objects.filter(stud = s[0])
        type = "stud"
        return render(request,'login/student.html',{"student": request.user ,"mycourses":myc,"courses": courses.objects.filter()})


def auth(request):
    u = request.POST.get('username', ' ')
    p = request.POST.get('password', ' ')
    user = authenticate(username=u, password=p)
    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect('/login/loggedin')
    else:
        messages.add_message(request, messages.SUCCESS, 'Unable to login either User name or password is incorrect!!')
        return HttpResponseRedirect('/login')

def addct(request):
    n = request.POST.get('name','')
    try:
        c = int(request.POST.get('credit',''))
    except:
        return HttpResponseRedirect("/login/loggedin")
    i = request.POST.get('info','')

    if n == '' or c == '' or i == '':
        print("yoyo")
        return HttpResponseRedirect("/login/loggedin")
    else:
        p = courses.objects.filter(name = 'n')
        if p:
            return HttpResponseRedirect("/login/loggedin")
        else:
            t = courses()
            t.name = n
            t.credit = c
            t.Inf = i
            k = teacher.objects.filter(user = request.user)
            t.teacher = k[0]
            try:
                t.save()
            except:
                messages.add_message(request, messages.SUCCESS,
                                     'Course Exists!!')
            return HttpResponseRedirect("/login/loggedin")

def selectprof(request):
    if request.method == 'GET':
        course = request.GET.get('course')
        print(course)
        c = courses.objects.filter(name = course)
        print(c[0].Inf)
        s = student.objects.filter(user = request.user)
        d = sc.objects.filter(course = c[0] , stud = s[0])
        try:
            a = d[0]
            return render(request,'login/coursedetails.html',{"course": c[0],"a":a,"student":request.user})
        except:
            return render(request,'login/coursedetails.html',{"course": c[0],"a":"","student":request.user})




def addcs(request):
    coursen = request.GET.get('course')
    course = courses.objects.filter(name = coursen)
    user1 = request.user
    stud1 = student.objects.filter(user = user1)[0]
    print(stud1)
    print(course)
    a = sc()
    a.stud = stud1
    a.course = course[0]
    a.grade = 0
    a.date = datetime.date.today()
    a.time = datetime.datetime.now().time()
    a.save()
    return HttpResponseRedirect("/login/loggedin")

def removesc(request):
    coursen = request.GET.get('course')
    course = courses.objects.filter(name = coursen)
    s = student.objects.filter(user=request.user)

    cs = sc.objects.filter(course = course[0],stud = s[0])
    cs[0].delete()
    return HttpResponseRedirect("/login/loggedin")

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')

def deletetc(request):
    coursed = request.GET.get('course')
    c = courses.objects.filter(name = coursed)
    c.delete()
    return HttpResponseRedirect("/login/loggedin")

def addmessage(request):
    print(datetime.datetime.now().time())
    print(datetime.date.today())
    course = request.GET.get('course')
    if request.method == 'POST':
        a = message()
        a.course = courses.objects.filter(name= request.POST.get('course'))[0]
        a.subject = request.POST.get('title')
        a.msg = request.POST.get('message')
        a.date = datetime.date.today()
        a.time = datetime.datetime.now().time()
        a.save()
        return HttpResponseRedirect("/login/loggedin")
    else:
        messagesc = message.objects.filter(course = courses.objects.filter(name = course)[0])
        return render(request,'login/addmessage.html',{"course": course,"messagesc": messagesc})

def studentmessage(request):
    scs = sc.objects.filter(stud=student.objects.filter(user=request.user)[0])
    coursess = []
    for scc in scs:
        c = {"course": scc.course,"message":""}
        messagesd = message.objects.filter(course = scc.course)
        d = []
        for messag in messagesd:
            if messag.date > scc.date or (messag.date == scc.date and messag.time > scc.time):
                d.append(messag)

        c["message"] = d
        coursess.append(c)

    return render(request,'login/studentmsg.html',{"courses":coursess,"student":request.user})