from django.forms import ModelForm
from zpapp.models import Worker

class AddWorker (ModelForm):
    class Meta:
        model = Worker
        fields = ['name','surname','patronymic','address','index','tel',
                  'ip_number','score_number','mfo']