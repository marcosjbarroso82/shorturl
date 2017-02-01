from django.http.response import HttpResponseRedirect
from django.views.generic.detail import BaseDetailView
from .models import DeviceUrl, ShortUrl
from user_agents import parse


class ShortUrlDetailView(BaseDetailView):
    model = ShortUrl

    def get(self, request, *args, **kwargs):
        device = None

        user_agent = parse(request.environ.get('HTTP_USER_AGENT'))
        obj = self.get_object()
        redirect_url = obj.target

        if user_agent.is_mobile:
            device = 'mobile'
        elif user_agent.is_tablet:
            device = 'tablet'
        elif user_agent.is_pc:
            device = 'desktop'

        if device:
            device_url = obj.get_device_url(device)
            device_url.counter += 1
            device_url.save()
            redirect_url = device_url.target

        obj.counter += 1
        obj.save()

        return HttpResponseRedirect(redirect_url)
