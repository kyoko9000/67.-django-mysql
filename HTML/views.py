from django.shortcuts import render


# Create your views here.
def HTML(request):
    return render(request, "HTML/gui.html")
