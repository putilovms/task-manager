from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


class StatusesListView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'statuses/statuses.html'
        return render(request, template_name=template_name, context={})


class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Status create')


class StatusUpdateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Status update')


class StatusDeleteView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Status delete')
