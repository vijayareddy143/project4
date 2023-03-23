from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':300,'b':200,'c':100}
    return render(request,'conditions.html',context=d)