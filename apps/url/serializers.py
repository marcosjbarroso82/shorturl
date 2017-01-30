from django.db.transaction import atomic
from rest_framework import serializers

from .models import ShortUrl, DeviceUrl


class ShortUrlModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceUrl
        fields = ('id', 'target', 'counter')
        read_only_fields = ('id', 'counter',)


class UrlModelSerializer(serializers.ModelSerializer):
    mobile_url = ShortUrlModelSerializer(required=False)
    tablet_url = ShortUrlModelSerializer(required=False)
    desktop_url = ShortUrlModelSerializer(required=False)

    class Meta:
        fields = '__all__'
        model = ShortUrl

    @atomic
    def create(self, validated_data):
        mobile_url = validated_data.pop('mobile_url', None)
        tablet_url = validated_data.pop('tablet_url', None)
        desktop_url = validated_data.pop('desktop_url', None)
        instance = ShortUrl.objects.create(**validated_data)

        # Create related DeviceUrls
        if mobile_url:
            instance.mobile_url = mobile_url.get('target')
            instance.save()
        if tablet_url:
            instance.tablet_url = tablet_url.get('target')
            instance.save()
        if desktop_url:
            instance.desktop_url = desktop_url.get('target')
            instance.save()

        return instance

    @atomic
    def update(self, instance, validated_data):
        mobile_url = validated_data.pop('mobile_url', None)
        tablet_url = validated_data.pop('tablet_url', None)
        desktop_url = validated_data.pop('desktop_url', None)

        # Update Url fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Update relate DeviceUrls
        if mobile_url:
            instance.mobile_url = mobile_url.get('target')
        if tablet_url:
            instance.tablet_url = tablet_url.get('target')
        if desktop_url:
            instance.desktop_url = desktop_url.get('target')

        instance.save()

        return instance


