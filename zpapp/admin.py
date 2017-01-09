from django.contrib import admin
from django.core.urlresolvers import reverse
from zpapp.models import Worker, Salary


@admin.register(Worker)
class WorkerAdmin (admin.ModelAdmin):
    list_display = ('surname', 'name', 'tel', 'remove_button')
    search_fields = ('surname', 'name', 'tel', 'ip_number')
    list_filter = ('surname', 'name',  'tel')


    def remove_button(self, obj):
        return '<a class="button" href="{}">Edit</a>'.format(reverse('admin:zpapp_worker_change', args=[obj.pk]))

    remove_button.short_description = 'Actions'
    remove_button.allow_tags = True


@admin.register(Salary)
class SalaryAdmin (admin.ModelAdmin):
    list_display = ('worker', 'salary_uah', 'button')
    search_fields = ('worker', 'salary_uah')
    list_filter = ('worker', 'salary_uah')

    def button(self, obj):
        return '<a class="button" href="{}">Print</a>'.format(reverse('act', args=[obj.worker.id]))

    button.short_description = 'Actions'
    button.allow_tags = True



