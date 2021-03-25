from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from orolaser.models import *
from orolaser.serializer import *




@api_view(['GET'])
def banner_collection(request):
    if request.method == 'GET':
        banners = Banner.objects.all()
        serializer = BannerSerializer(banners, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def banner_element(request, pk):
    try:
        banner = Banner.objects.get(pk=pk)
    except Banner.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BannerSerializer(banner)
        return Response(serializer.data)\

@api_view(['GET'])
def unit_collection(request):
    if request.method == 'GET':
        units = Units.objects.all()
        serializer = UnitSerializer(units, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def unit_element(request, pk):
    try:
        unit = Units.objects.get(pk=pk)
    except Units.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UnitSerializer(unit)
        return Response(serializer.data)

@api_view(['POST'])
def save_token(request):
    if request.method == 'POST':
        token = request.data.get('token')
        if Token.objects.all().filter(token=token):
            return HttpResponse(status=200)
        else:
            token = Token(token=token)
            token.save()
            serializer = TokenSerializer(token)
            return Response(serializer.data)
    else:
        return HttpResponse(status=300)