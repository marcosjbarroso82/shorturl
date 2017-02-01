from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from apps.url.apis import DeviceUrlModelViewSet, ShortUrlModelViewSet


router = DefaultRouter(trailing_slash=False)

router.register(r'urls', ShortUrlModelViewSet, base_name='short-urls')
router.register(r'device-urls', DeviceUrlModelViewSet, base_name='device-short-urls')


urlpatterns = [
    # Include router api
    url(r'^', include(router.urls)),
]
