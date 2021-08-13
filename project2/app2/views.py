from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_hai(request):
    return HttpResponse("app2 hai view function ")
