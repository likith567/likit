from django.shortcuts import render


# Create your views here.
def nani(request):
  return render(request,'app1/nani.html')