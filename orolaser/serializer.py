from rest_framework import serializers
from orolaser.models import *


class BannerSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    class Meta:
        model = Banner
        fields = ('id', 'name', 'photo_url', 'price', 'description', 'oroClub')

    def get_photo_url(self, banner):
        request = self.context.get('request')
        photo_url = banner.photo.url
        return photo_url


class UnitSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    class Meta:
        model = Units
        fields = ('id', 'name', 'photo_url', 'address', 'lat', 'long','opening_hours')

    def get_photo_url(self, unit):
        request = self.context.get('request')
        photo_url = unit.photo.url
        return photo_url

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('id', 'token')