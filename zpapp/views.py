from django.shortcuts import render, redirect
from zpapp.forms import AddWorker
from django.views.decorators.csrf import csrf_exempt

from zpapp.models import Salary, Worker


@csrf_exempt
def home (request):
    if not request.user.is_authenticated():
        return redirect('/admin/')
    workers = Worker.objects.all()
    return render(request, 'zpapp/home.html', {'workers': workers})


def add_worker (request):
    if not request.user.is_authenticated():
        return redirect('/admin/' )
    form = AddWorker(request.POST)

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect('home')

    return render(request, 'zpapp/add_worker.html', {'form': form})


def acts (request, obj):
    if not request.user.is_authenticated():
        return redirect('/admin/')
    salary = Salary.objects.filter(worker=obj).values()
    workers = Worker.objects.filter(id=obj).values()
    return render(request, 'zpapp/act.html', {'workers':workers, 'salary':salary })
