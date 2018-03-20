from builtins import print

import os
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from website import settings
from .models import Stock, File
from .serializers import StockSerializer, FileSerializer
from rest_framework.decorators import api_view


# class StockList(APIView):

@api_view(['GET', 'POST'])
def stoList(request):
    if request.method == 'GET':
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = StockSerializer(data=data)

        # ticker = request.data['ticker']
        # open = request.data['open']
        # close = request.data['close']
        # vloume = request.data['vloume']
        # data = ticker + open + close + vloume
        # return Response(data, status=status.HTTP_201_CREATED)
        # serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # def get(self, request):
        #     stocks = Stock.objects.all()
        #     serializer = StockSerializer(stocks, many=True)
        #     return Response(serializer.data)
        #
        # def post(self, request, format=None):
        #     serializer = StockSerializer(data=request.DATA)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.DATA, status=status.HTTP_201_CREATED)
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def fileUpload(request):
    if request.method == 'GET':
        files = File.Objects.all();
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        filedata = request.data['file']
        id = request.data['id']

        # name = request.data['name']
        runner_dir = os.path.join(settings.MEDIA_ROOT)
        if not os.path.isdir(runner_dir):
            os.makedirs(runner_dir)
        dest_file_path = os.path.join(runner_dir, filedata.name)
        with open(dest_file_path, 'wb') as runner_file:
            for chunk in filedata.chunks():
                runner_file.write(chunk)

        return Response(dest_file_path + id, status=status.HTTP_201_CREATED)
        # file_serizer = FileSerializer(data= request.data)
        # if file_serizer.is_valid():
        #     file_serizer.save()
        #     return Response(dest_file_path, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(file_serizer.errors, status=status.HTTP_400_BAD_REQUEST)
