from django.http.response import HttpResponseRedirect
from django.views.generic.detail import BaseDetailView
from .models import DeviceUrl, ShortUrl
from user_agents import parse
from django.db.transaction import atomic


class ShortUrlDetailView(BaseDetailView):
    model = ShortUrl

    @atomic
    def get(self, request, *args, **kwargs):
        device = None

        user_agent = parse(request.environ.get('HTTP_USER_AGENT'))
        obj = self.get_object(queryset=ShortUrl.objects.select_for_update().all())
        redirect_url = obj.target

        if user_agent.is_mobile:
            device = 'mobile'
        elif user_agent.is_tablet:
            device = 'tablet'
        elif user_agent.is_pc:
            device = 'desktop'

        if device:
            device_url = obj.device_urls.select_for_update().filter(type=device).first()
            if device_url:
                device_url.counter += 1
                device_url.save()
                redirect_url = device_url.target

        obj.counter += 1
        obj.save()

        return HttpResponseRedirect(redirect_url)
