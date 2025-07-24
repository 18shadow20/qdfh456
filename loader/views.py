import json
from datetime import datetime

from django.shortcuts import render
from django.contrib import messages
from .models import Record
from .forms import JsloadForm

def upload_json(request):
    if request.method == 'POST':
        form = JsloadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                messages.error(request, 'Файл не является JSON')
                return render(request, 'loader/loader.html', {'form':form})

            valid_records = []

            for i in data:
                name = i.get('name')
                date_str = i.get('date')

                if not name or not date_str:
                    messages.error(request, "Отсутствует нужный ключ")
                    return render(request, 'loader/loader.html', {'form':form})

                if len(name) >= 50:
                    messages.error(request,'Поле слишком длинное')
                    return render(request, 'loader/loader.html', {'form':form})

                try:
                    date = datetime.strptime(i['date'], "%Y-%m-%d_%H:%M")
                except ValueError:
                    messages.error(request,'Неверный формат даты')
                    return render(request, 'loader/loader.html', {'form':form})

                valid_records.append(Record(name=name,date=date))

            Record.objects.bulk_create(valid_records)


        else:
            messages.error(request,'Форма не валидна')
    else:
        form = JsloadForm()

    return render(request, 'loader/loader.html', {'form':form})


def all_records(request):
    records = Record.objects.all()
    return render(request, 'loader/all_records.html', {'records':records})


