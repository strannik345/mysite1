from django.shortcuts import render
from django.http import HttpResponse

from .models import temperature

import datetime

def add(request, temp):
	now = datetime.datetime.strptime(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),"%d/%m/%Y %H:%M:%S")
	curr_temperature = temperature.objects.create(date = now, temperature = temp)
	curr_temperature.save()
	print(temp, now)
	return HttpResponse()


# Create your views here.
