from django.conf.urls import url, include
from django.contrib import admin

from apps.url.views import ShortUrlDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('shorturl.urls_api', namespace='api')),
    # url(r'^su/(?P<pk>[0-9a-z-]+)', ShortUrlDetailView.as_view(), name='short-url' ),
    url(r'^su/(?P<pk>[-\w]+)/$', ShortUrlDetailView.as_view(), name='article-detail'),
]


from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()