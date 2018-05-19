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
        dicts = []
        # for kassa in kassas:
        #     data_dict = dict(kassa=nomer, persons=person_counter, date='date', status='busy')
        #     dicts.append(data_dict)
        data_dict = dict(kassa=1, persons=person_counter, date='date', status='busy')
        data_dict2 = dict(kassa=1, persons=person_counter, date='date', status='busy')
        dicts = [data_dict, data_dict2]
        json_dict = dict(data=dicts)
        json_data = json.dumps(json_dict, indent=4)
        return HttpResponse(json_data
            # {
                    # 'data': [
                    #         {
                    #             'kassa': 1,
                    #             'persons': person_counter,
                    #             'date': date
                    #             'status': 'busy'
                    #         },
                    #         {
                    #             'kassa': 2,
                    #             'persons': person_counter,
                    #             'date': 'free'
                    #         },
                    #         {
                    #             'kassa': 3,
                    #             'persons': person_counter,
                    #             'date': 'free'
                    #         }
                    #
                    #         ],

                             # }
        )

    else:
        return JsonResponse({'status': 'failed'})

