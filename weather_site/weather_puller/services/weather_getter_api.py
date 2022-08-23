import requests
import math


# оставлю здесь, а не в окружении, т.к. данные мне неважны
OPENWEATHERMAP_APPID = '2bd5a3be03f98aba9b1cdfea7ecb3cde'

def get_all_weather_data(city_name: str) -> dict:
	''' Возвращает температуру и полное описание '''

	try:
		data = _get_weather_data_dict(city_name)
		temp_c = _get_temperature_celcius(data)
		description = _get_description(data)
		res_dict = {'city_name': city_name, 'temp_c': temp_c, 'description': description}
	except:
		res_dict = None
	finally:
		return res_dict


def _get_weather_data_dict(city_name: str) -> dict:
	''' Получает по API json-данные о погоде, 
	конвертирует в dict и возвращает его'''

	url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHERMAP_APPID}'
	
	return requests.get(url).json()


def _get_temperature_celcius(weather_data: dict) -> str:
	''' Возвращает температуру из словаря 
	данных о погоде '''

	temp_k = float(weather_data['main']['temp']) 
	temp_c = math.floor(temp_k - 273.15)
	return str(temp_c)


def _get_description(weather_data: dict) -> str:
	''' Возвращает описание из словаря 
	данных о погоде '''

	return weather_data['weather'][0]['description']

