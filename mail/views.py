from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "mail/home.html")


def signin(request):
    print("sign in")
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        user = request.POST['user']
        email = request.POST['email']
        password = request.POST['pass']
        print("fname", fname, "lname", lname)

        my_user = User.objects.create_user(user, email, password)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.is_staff = "1"
        my_user.save()
        # return HttpResponseRedirect("http://127.0.0.1:8000/signin/")
        # return HttpResponse("success")
        messages.success(request, "create user success full")
        return render(request, "mail/login.html")

    return render(request, "mail/signin.html")


def login(request):
    print("log in")
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['pass']
        print("user", username, "pass", password)

        user = authenticate(username=username, password=password)
        if user is not None:
            print("ok chich")
            return render(request, "mail/inmail.html")
        else:
            messages.error(request, "user or pass wrong")

    return render(request, "mail/login.html")
