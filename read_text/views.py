from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def read_text(request):
    if request.method == "POST":
        rtext = request.POST['text']
        print("this text is: ", rtext)
        # return HttpResponse("success")
        return redirect('read_text')

    return render(request, "read_text/gui.html")


