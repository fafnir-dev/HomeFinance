from django.shortcuts import HttpResponse

import datetime


def index(request):
    now = datetime.datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
    html = f"Сегодня: {now}"
    return HttpResponse(html)
