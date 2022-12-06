from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Place1


# from .models import Place1
# Create your views here.
# def demo(request):
#     name='India'
#     return render(request,"home.html",{'obj':name})
#
# def addition(request):
#
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request, "result.html", {'result': res})
# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return render (request,"contact.html")

def demo(request):
    obj = Place.objects.all()
    obj1 = Place1.objects.all()

    return render(request, "index.html", {'result': obj, 'result1': obj1})
