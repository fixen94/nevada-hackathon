from django.http import StreamingHttpResponse, HttpResponse, JsonResponse
from django.shortcuts import render
from urllib.request import urlretrieve
import  json


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
    data = []
    if request.method == "POST":
        with open("data.txt", 'r', encoding='utf-8') as file:
            for line in file:
                data.append(line)
        json_data = json.dumps(data, sort_keys=True, indent=4)
        return JsonResponse(json_data)

