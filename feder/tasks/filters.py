# -*- coding: utf-8 -*-
from atom.filters import CrispyFilterMixin, AutocompleteChoiceFilter
from django.utils.translation import ugettext_lazy as _
import django_filters
from .models import Task


class TaskFilter(CrispyFilterMixin, django_filters.FilterSet):
    case = AutocompleteChoiceFilter('CaseAutocomplete')
    questionary = AutocompleteChoiceFilter('QuestionaryAutocomplete')
    case__institution = AutocompleteChoiceFilter('InstitutionAutocomplete')
    case__monitoring = AutocompleteChoiceFilter('MonitoringAutocomplete')
    created = django_filters.DateRangeFilter(label=_("Creation date"))
    form_class = None

    def __init__(self, *args, **kwargs):
        super(TaskFilter, self).__init__(*args, **kwargs)
        self.filters['name'].lookup_type = 'icontains'

    class Meta:
        model = Task
        fields = ['name', 'case', 'questionary', 'case__institution', ]
        order_by = ['created', ]
