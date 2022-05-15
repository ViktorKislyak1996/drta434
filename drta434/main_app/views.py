from django.core import serializers
from django.shortcuts import render, redirect
from .forms import AddPostForm
from .models import Main
import json


def index(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        # Проверка валидности формы
        if form.is_valid():
            # Сбор данных из формы
            input_value = form.cleaned_data['name']
            # Преобразование в json
            data = json.dumps(input_value, ensure_ascii=False).strip(' " ')
            Main.objects.create(data=data)
            # Сбор данных из других форм
            for number in range(1, len(request.POST)-1):
                input_name = 'name' + str(number)
                input_value = request.POST[input_name]
                # Проверка на пустое поле ввода
                if input_value:
                    data = json.dumps(input_value, ensure_ascii=False).strip(' " ')
                    Main.objects.create(data=data)
        return redirect('output')
    else:
        form = AddPostForm()
    return render(request, 'main_app/index.html', {'form': form})

def output(request):
    # Выборка данных из базы данных
    queryset = Main.objects.all().values('data')
    json_list = list(queryset)
    return render(request, 'main_app/output.html', {'json_list' : json_list})
