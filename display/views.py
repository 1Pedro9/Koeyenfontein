from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import transaction
from datetime import datetime

# Create your views here.
def index(requests):
    return render(requests, "index.html", {"name": "Pedro"})

def contact(requests):
    return render(requests, "contact.html")