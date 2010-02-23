from django.shortcuts import render_to_response
from django.http import HttpResponse
#from Passwords.models import *

    
def testDisplay(request):
    return HttpResponse("test")
