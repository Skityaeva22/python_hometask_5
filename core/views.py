from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def renderDate(request):
    now = datetime.now()
    html = "<html><body>Текущая дата: %s</body></html>" % now
    return HttpResponse(html)