# from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class TasksListView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Tasks')


class TasksCreateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Task create')


class TasksDeleteView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Task delete')


class TasksUpdateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Task update')


class TaskView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Task view')
