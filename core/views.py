from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import render
from urllib.request import urlretrieve

# Create your views here.


def show_data(request):
    data = []
    destination = 'data.txt'
    url = 'http://urconsult27.ru/robots.txt'
    urlretrieve(url, destination)
    with open("data.txt", 'r', encoding='utf-8') as file:
        for line in file:
            data.append(line)
    return render(request, 'index.html', {
        'data': data,
    })
