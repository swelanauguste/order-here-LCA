import os

from django.shortcuts import render


def index(request):
    # get_ip = os.system("curl ipinfo.io/ip")
    # print(get_ip)
    ip = request.META.get('REMOTE_ADDR')
    print(ip)
    context = {"ip": ip}
    return render(request, "index.html", context)
