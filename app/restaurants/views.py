import os

from django.shortcuts import render


def index(request):
    ip = request.META.get('REMOTE_ADDR')
    context = {"ip": ip}
    return render(request, "index.html", context)
