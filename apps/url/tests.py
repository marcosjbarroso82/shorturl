from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import ShortUrl, DeviceUrl
from rest_framework.test import APIClient, RequestsClient


class TestShortUrlTests(APITestCase):
    def test_create_short_url_without_device(self):
        """
        Ensure we can create a new url without device specification
        """
        client = RequestsClient()
        response = client.post('http://testserver/api/v1/urls', json={'target': 'http://example.com'})
        assert response.status_code == 201

        short_url = dict(response.json())
        self.assertIsNone(short_url.get('mobile_url'))
        self.assertIsInstance(short_url.get('target'), str)

    def test_update_short_url(self):
        """
        Ensure we can update an url without device specification
        """
        old_target = 'http://old.com'
        new_target = 'http://new.com'

        old_short_url = ShortUrl.objects.create(target=old_target)

        client = RequestsClient()
        response = client.patch('http://testserver/api/v1/urls/%s' % old_short_url.id, json={'target': new_target})
        assert response.status_code == 200

        short_url = dict(response.json())
        self.assertEqual(short_url.get('target'), new_target)

    def test_create_short_url_with_device(self):
        """
        Ensure we can create a new url with device specification
        """
        target = 'http://exmaple.com'
        mobile_target = 'http://mobile.exmaple.com'
        tablet_target = 'http://tablet.exmaple.com'
        desktop_target = 'http://desktop.exmaple.com'
        data = {
            'target': target,
            'mobile_url': {'target': mobile_target},
            'tablet_url': {'target': tablet_target},
            'desktop_url': {'target': desktop_target},
        }

        client = RequestsClient()
        response = client.post('http://testserver/api/v1/urls', json=data)

        assert response.status_code == 201

        short_url = dict(response.json())
        self.assertIsNotNone(short_url.get('mobile_url'))
        self.assertIsNotNone(short_url.get('tablet_url'))
        self.assertIsNotNone(short_url.get('desktop_url'))

        mobile_url = short_url.get('mobile_url')
        tablet_url = short_url.get('tablet_url')
        desktop_url = short_url.get('desktop_url')

        self.assertEqual(mobile_url.get('target'), mobile_target)
        self.assertEqual(tablet_url.get('target'), tablet_target)
        self.assertEqual(desktop_url.get('target'), desktop_target)



    def test_update_short_url_with_device(self):
        """
        Ensure we can update an url with device specification
        """
        old_target = 'http://old.com'
        old_mobile_target = 'http://mobile.old.com'
        old_tablet_target = 'http://tablet.old.com'
        old_desktop_target = 'http://desktop.old.com'

        new_target = 'http://new.com'
        new_mobile_target = 'http://mobile.new.com'
        new_tablet_target = 'http://tablet.new.com'
        new_desktop_target = 'http://desktop.new.com'

        new_data = {
            'target': new_target,
            "mobile_url": {"target": new_mobile_target},
            "tablet_url": {"target": new_tablet_target},
            "desktop_url": {"target": new_desktop_target}
        }


        old_short_url = ShortUrl.objects.create(target=old_target)
        old_short_url.mobile_url = old_mobile_target
        old_short_url.tablet_url = old_tablet_target
        old_short_url.desktop_url = old_desktop_target
        old_short_url.save()

        client = RequestsClient()
        response = client.patch('http://testserver/api/v1/urls/%s' % old_short_url.id, json=new_data)
        assert response.status_code == 200

        short_url = dict(response.json())
        self.assertEqual(short_url.get('target'), new_target)
        self.assertEqual(short_url.get('mobile_url').get('target'), new_mobile_target)
        self.assertEqual(short_url.get('tablet_url').get('target'), new_tablet_target)
        self.assertEqual(short_url.get('desktop_url').get('target'), new_desktop_target)



