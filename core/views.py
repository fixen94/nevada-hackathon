from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import render

# Create your views here.


def show_data(request):
    data = []
    with open("data.txt", 'r', encoding='utf-8') as file:
        for line in file:
            data.append(line)
    return render(request, 'index.html', {
        'data': data,
    })
