from django.shortcuts import render

def candidates_home(request):
    return render( request, "candidates_home.html", {})