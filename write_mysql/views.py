from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def signin(request):
    print("run sign in")
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
        return HttpResponseRedirect("http://127.0.0.1:8000/signin/")
        # return HttpResponse("success")

    return render(request, "write_mysql/signin.html")
