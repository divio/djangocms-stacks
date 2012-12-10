# -*- coding: utf-8 -*-
from django_select2.fields import AutoModelSelect2Field
from stacks.models import Stack


class StackSearchField(AutoModelSelect2Field):
    search_fields = ('name__icontains', 'code__icontains',)
    queryset = Stack.objects
