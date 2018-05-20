from django.http import StreamingHttpResponse, HttpResponse, JsonResponse
from django.shortcuts import render
import json
from django.core import serializers
import re
from .models import Kassa, Time



def show_data(request):
    data = []
    with open("C:/Users/fixen/Dropbox/Samberi/new.txt", 'r', encoding='utf-8') as file:
        for line in file:
            data.append(line)
    with open("C:/Users/fixen/Dropbox/Samberi/output2.txt", 'w', encoding='utf-8') as file:
        file.writelines(data)

    date = data[0].strip()
    date_entry = Time.objects.create_time(date)

    kassas = []
    for idx, line in enumerate(data):
        if 'kassa' in line:
            info_start = idx
        if '>' in line:
            info_end = idx
            info = data[info_start:info_end+1]
            kassas.append(info)

    dicts_lst = list()
    for kassa in kassas:
        kassa_dict = dict()
        person_counter = 0
        kassa_no = 0
        persons = "free"
        for line in kassa:
            if 'kassa' in line:
                kassa_no = re.findall(r'\d+', line)
                kassa_no = kassa_no[0]
            if 'person' in line:
                person_counter += 1
        persons = person_counter
        if persons > 5:
            status = 'busy'
            kassa_entry = Kassa.objects.create_kassa(kassa_no, persons, status, date_entry)

    final_kassa = Time.objects.all()[0]
    print(final_kassa)
    return render(request, 'index.html', {
        date: 'date',
        final_kassa: 'final_kassa',
    })


def update(request):
    if request.method == "POST":
        data = []
        with open("C:/Users/fixen/Dropbox/Samberi/output.txt", 'r', encoding='utf-8') as file:
            for line in file:
                data.append(line)
        old_data = []
        with open("C:/Users/fixen/Dropbox/Samberi/output2.txt", 'r', encoding='utf-8') as file:
            for line in file:
                old_data.append(line)
        if old_data == data:
            return JsonResponse({'status': 'old'})

        person_counter = 0
        for line in data:
            if 'person' in line:
                person_counter += 1

        dicts = []
        # for kassa in kassas:
        #     data_dict = dict(kassa=nomer, persons=person_counter, date='date', status='busy')
        #     dicts.append(data_dict)
        data_dict = dict(kassa=1, persons=person_counter, date='date', status='busy')
        data_dict2 = dict(kassa=2, persons=person_counter, date='date', status='free')
        dicts = [data_dict, data_dict2]
        json_dict = dict(data=dicts)
        json_data = json.dumps(json_dict, indent=4)
        return HttpResponse(json_data)

    else:
        return JsonResponse({'status': 'failed'})

