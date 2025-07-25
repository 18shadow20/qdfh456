import json
from django.shortcuts import render
from django.contrib import messages
from .models import Record
from .forms import JsloadForm
from .utils import validate_json_record

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
            for record in data:
                is_valid, result = validate_json_record(record)
                if not is_valid:
                    messages.error(request, result)
                    return render(request, 'loader/loader.html', {'form': form})
                valid_records.append(result)

            Record.objects.bulk_create(valid_records)


        else:
            messages.error(request,'Форма не валидна')
    else:
        form = JsloadForm()

    return render(request, 'loader/loader.html', {'form':form})


def all_records(request):
    records = Record.objects.all()
    return render(request, 'loader/all_records.html', {'records':records})


