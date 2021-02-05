import requests
from django.shortcuts import render

from .models import City
from .forms import CityForm


def index(request):
    cities = City.objects.all()
    api_key = 'faa84ad5b1e034b27f5f673930beec43'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={0}&units=metric&appid={1}'
    all_cities = []

    if request.method == 'POST':
        args = request.POST['name'].split(' ')
        if args[0] == 'add':
            if City.objects.filter(name=args[1]) == '<QuerySet []>':
                pass
            else:
                city_code_status = requests.get(url.format(args[1], api_key)).json()['cod']
                if city_code_status == '404':
                    pass
                else:
                    correct_request = dict(request.POST)
                    correct_request['name'] = args[1]
                    form = CityForm(correct_request)
                    form.save()
        if args[0] == 'rm':
            if args[1] == 'all':
                City.objects.all().delete()
            else:
                City.objects.filter(name=args[1]).delete()
        if args[0] == 'get':
            if args[1] == 'json':
                generate_context(cities, all_cities, url, api_key)
                return render(request, 'all_cities.html', {'cities': all_cities})

    form = CityForm()

    generate_context(cities, all_cities, url, api_key)
    context = {'info': all_cities, 'form': form}
    return render(request, 'weather.html', context)


def generate_context(cities, cities_list, url, api_key):
    for city in cities:
        response = requests.get(url.format(city.name, api_key)).json()
        city_info = {
            'city': city.name,
            'temp': response['main']['temp'],
            'icon': response['weather'][0]['icon']
        }
        cities_list.append(city_info)