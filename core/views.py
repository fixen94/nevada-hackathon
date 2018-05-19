from django.http import StreamingHttpResponse, HttpResponse, JsonResponse
from django.shortcuts import render
from urllib.request import urlretrieve
import json
from django.core import serializers


def show_data(request):
    data = []
    with open("C:/Users/fixen/Dropbox/Samberi/output.txt", 'r', encoding='utf-8') as file:
        for line in file:
            data.append(line)
    print(data)
    person_counter = 0
    for line in data:
        if 'person' in line:
            person_counter += 1

    return render(request, 'index.html', {
        'data': data,
        'person_counter': person_counter,
    })


def update(request):
    if request.method == "POST":
        data = []
        with open("C:/Users/fixen/Dropbox/Samberi/output.txt", 'r', encoding='utf-8') as file:
            for line in file:
                data.append(line)
        person_counter = 0
        for line in data:
            if 'person' in line:
                person_counter += 1
        # json_data = json.dumps({'persons': person_counter}, indent=4)
        return JsonResponse({'persons': person_counter
                             })

    else:
        return JsonResponse({'status': 'failed'})

