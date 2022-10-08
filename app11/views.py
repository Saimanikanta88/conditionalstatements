from django.shortcuts import render

# Create your views here.
def flowcontrol(request):
    d={'a':50,'b':10,'c':100}
    return render(request,'conditional.html',context=d)
