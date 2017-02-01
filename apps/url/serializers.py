from django.db.transaction import atomic
from rest_framework import serializers

from .models import ShortUrl, DeviceUrl


class DeviceUrlModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceUrl
        fields = ('id', 'target', 'counter', 'type')
        read_only_fields = ('id', 'counter', 'type')

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class UrlModelSerializer(serializers.ModelSerializer):
    mobile_url = DeviceUrlModelSerializer(required=False)
    tablet_url = DeviceUrlModelSerializer(required=False)
    desktop_url = DeviceUrlModelSerializer(required=False)

    class Meta:
        fields = '__all__'
        model = ShortUrl

    @atomic
    def create(self, validated_data):
        mobile_url = validated_data.pop('mobile_url', None)
        tablet_url = validated_data.pop('tablet_url', None)
        desktop_url = validated_data.pop('desktop_url', None)
        instance = ShortUrl.objects.create(**validated_data)

        # Create Device Urls
        if mobile_url:
            self.create_or_update_device_url(url=instance, type='mobile', data=mobile_url)
        if tablet_url:
            self.create_or_update_device_url(url=instance, type='tablet', data=tablet_url)
        if desktop_url:
            self.create_or_update_device_url(url=instance, type='desktop', data=desktop_url)

        return instance

    @atomic
    def update(self, instance, validated_data):
        mobile_url = validated_data.pop('mobile_url', None)
        tablet_url = validated_data.pop('tablet_url', None)
        desktop_url = validated_data.pop('desktop_url', None)

        # Update Url fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Update or Create Device Urls
        if mobile_url:
            self.create_or_update_device_url(url=instance, device_url=instance.mobile_url, type='mobile', data=mobile_url)
        if tablet_url:
            self.create_or_update_device_url(url=instance, device_url=instance.tablet_url, type='tablet', data=tablet_url)
        if desktop_url:
            self.create_or_update_device_url(url=instance, device_url=instance.desktop_url, type='desktop', data=desktop_url)

        instance.save()
        return instance

    @staticmethod
    def create_or_update_device_url(url=None, device_url=None, type='', data=None):
        if device_url and type:
            # Upadate Device Url
            serializer = DeviceUrlModelSerializer(instance=device_url, data=data)
            serializer.is_valid()
            serializer.save()
        elif url and data:
            # Create Device Url
            serializer = DeviceUrlModelSerializer(data=data)
            serializer.is_valid()
            serializer.save(url=url, type=type)
