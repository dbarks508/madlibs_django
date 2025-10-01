from django.shortcuts import render
from django.http import HttpResponse

def welcome_page(self):
    return HttpResponse("Welcome to madlibs!")
