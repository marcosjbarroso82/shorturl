from rest_framework import viewsets

from .models import ShortUrl, DeviceUrl
from .serializers import UrlModelSerializer, DeviceUrlModelSerializer


class ShortUrlModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for ShortUrl REST API. Methods allowed are: POST, GET, PUT, PATCH.


    Example response for Listing:
    method: GET
    url: http://server.com/api/v1/urls
    reponse:
        [
      {
		"id": 1,
        "hash": "35C07D",
        "mobile_url": {
          "id": 1,
          "target": "http://mobile.youtube.com",
          "counter": 0
        },
        "tablet_url": null,
        "desktop_url": null,
        "created_at": "2017-01-30T00:55:26.697105Z",
        "updated_at": "2017-01-30T00:55:26.699139Z",
        "target": "http://youtube.com",
        "counter": 0
      }
    ]

    Example Request for Creating:
    method: POST
    url: http://server.com/api/v1/urls
    headers:[
        Content-Type: application/json
    ]
    payload:
    {
	"target": "http://youtube.com",
	"mobile_url": { "target": "http://mobile.youtube.com"}
    }


    Example Request for Updating:
    method: PATCH
    url: http://server.com/api/v1/urls/35C07D
    headers:[
        Content-Type: application/json
    ]
    payload:
    {
	"target": "http://youtube.com",
	"mobile_url": { "target": "http://mobile.youtube.com"}
    }

    """
    queryset = ShortUrl.objects.all()
    lookup_field = 'hash'
    serializer_class = UrlModelSerializer
    # http_method_names = ['get', 'post']


class DeviceUrlModelViewSet(viewsets.ModelViewSet):
    queryset = DeviceUrl.objects.all()
    serializer_class = DeviceUrlModelSerializer
    # http_method_names = ['get']