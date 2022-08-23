from django.shortcuts import render
import datetime

import requests
from .services.weather_getter_api import get_all_weather_data
from .forms import *

def index(request):
	''' Главная и единственная страница '''

	if request.method == 'POST':
		form = CityForm(request.POST)
		if form.is_valid():
			context = {
			'city_info': get_all_weather_data(form.cleaned_data['city_name']),
			'form': form
			}
	elif request.method == 'GET':
		form = CityForm()
		context = {
		'city_info': None,
		'form': form
		}
	return render(request, 'index.html', context)