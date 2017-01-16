from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.contrib.admin.views.main import ChangeList
from django.core.urlresolvers import reverse
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from django.contrib.humanize.templatetags.humanize import intcomma

import os
import datetime

from Act.settings import BASE_DIR
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


class DateFilter(SimpleListFilter):
    title = 'Date'
    parameter_name = 'date'

    def lookups(self, request, model_admin):
        dates = set([c for c in model_admin.model.objects.dates('date', 'month')])

        return [(c, '{}'.format(datetime.datetime.strftime(c, '%B %Y'))) for c in sorted(dates, reverse=True)]

    def queryset(self, request, queryset):
        if self.value():
            date = datetime.datetime.strptime(self.value(), '%Y-%m-%d').date()

            return queryset.filter(date__month=date.month, date__year=date.year)
        else:
            return queryset


class MyChangeList(ChangeList):

    def get_results(self, *args, **kwargs):
        super(MyChangeList, self).get_results(*args, **kwargs)
        total = self.result_list.aggregate(total_salary=Sum('salary_uah'))['total_salary']
        self.total_count = '{} UAH'.format(intcomma(total))

@admin.register(Salary)
class SalaryAdmin (admin.ModelAdmin):

    def get_changelist(self, request):
        return MyChangeList

    list_display = ('worker', 'salary', 'dates', 'button_print')
    search_fields = ('worker', 'salary_uah', 'dates')
    list_filter = ('worker', DateFilter)
    actions = ['action_print']

    change_list_template = [os.path.join(BASE_DIR,'templates/admin/zpapp/salary/change_list.html')]

    def action_print(self, request, queryset):
        select = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        return HttpResponseRedirect("/act/{}".format("&".join(select)))
    action_print.short_description = 'Print'
    action_print.allow_tags = True


    def dates(self, obj):
        return obj.date.strftime("%d %B %Y")
    dates.short_description = 'Date Salary'


    def button_print (self, obj):
        return mark_safe('<a class="button" href="{}">Print</a>'.format(reverse('act', args=[obj.pk])))
    button_print.short_description = 'Actions'
    button_print.allow_tags = True

    def salary (self, obj):
        return '{} UAH'.format(intcomma(obj.salary_uah))