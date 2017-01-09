from django.contrib import admin
from django.core.urlresolvers import reverse
from zpapp.models import Worker, Salary


@admin.register(Worker)
class WorkerAdmin (admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'remove_button')
    search_fields = ('surname', 'name', 'patronymic')
    list_filter = ['surname']


    def remove_button(self, obj):
        return '<a class="button" href="{}">Delete</a>'.format(reverse('admin:zpapp_worker_delete', args=[obj.pk]))

    remove_button.short_description = 'Actions'
    remove_button.allow_tags = True


@admin.register(Salary)
class SalaryAdmin (admin.ModelAdmin):
    list_display = ('worker', 'salary_uah', 'dates', 'button')
    search_fields = ('worker', 'salary_uah', 'dates')
    list_filter = ('worker', 'date')

    def button(self, obj):
        return '<a class="button" href="{}">Print</a>'.format(reverse('act', args=[obj.pk]))

    button.short_description = 'Actions'
    button.allow_tags = True

    def dates(self, obj):
        return obj.date.strftime("%d %b %Y")

    dates.short_description = 'Date Salary'


