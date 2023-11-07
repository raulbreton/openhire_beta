from django.shortcuts import render

def employers_home(request):
    return render( request, "employers_home.html", {})