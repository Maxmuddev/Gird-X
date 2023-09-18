from django.shortcuts import render

# Create your views here.
def homeview(request):
    return render(request,"index.html")

def aboutview(request):
    return render(request,"about.html")
def worksview(request):
    return render(request,"works.html")
def contactview(request):
    return render(request,"contact.html")