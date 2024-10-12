from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError


class ProtectedMessageMixin:
    protected_error_message = ''

    def post(self, request, *args, **kwargs):
        self.request = request
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, self.protected_error_message)
        return HttpResponseRedirect(success_url)
