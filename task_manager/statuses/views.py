from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.views.generic.list import ListView
from task_manager.statuses.models import Statuses


class StatusesListView(ListView):
    model = Statuses
    template_name = 'statuses/statuses.html'


class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Status create')


class StatusUpdateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Status update')


class StatusDeleteView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Status delete')
