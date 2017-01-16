from django.contrib.humanize.templatetags.humanize import intcomma
from django.shortcuts import render, redirect
from zpapp.forms import AddWorker
from django.views.decorators.csrf import csrf_exempt

from zpapp.models import Salary, Worker


@csrf_exempt
def home (request):
    if not request.user.is_authenticated():
        return redirect('admin:login')
    workers = Worker.objects.all()
    return render(request, 'zpapp/home.html', {'workers': workers})


def add_worker (request):
    if not request.user.is_authenticated():
        return redirect('admin:login' )
    form = AddWorker(request.POST)

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect('home')

    return render(request, 'zpapp/add_worker.html', {'form': form})


def acts (request, obj):
    if not request.user.is_authenticated():
        return redirect('admin:login')
    ids = obj.split('&')
    workers = []

    for id in ids:
        salary = Salary.objects.get(id=id)
        worker = Worker.objects.get(id=salary.worker.pk)

        worker_dict = {
            'name': worker.name,
            'surname': worker.surname,
            'patronymic': worker.patronymic,
            'address': worker.address,
            'index': worker.index,
            'tel' : worker.tel,
            'ip_number' : worker.ip_number,
            'score_number': worker.score_number,
            'mfo' : worker.mfo,
            'contract': worker.contract,
            'date_contract': worker.date_contract,
            'service': worker.service,
            'salary_uah': '{}'.format(intcomma(salary.salary_uah)),
            'date': salary.date
        }
        workers.append(worker_dict)
    return render(request, 'zpapp/act.html', {'workers':workers })
