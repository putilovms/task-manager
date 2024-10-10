from django.http import HttpResponse
from django.views import View

# Create your views here.


class StatusesListView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Statuses')


class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Status create')


class StatusUpdateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Status update')


class StatusDeleteView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Status delete')
