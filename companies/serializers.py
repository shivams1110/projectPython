from rest_framework import serializers
from .models import Stock, File


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('ticker', 'open', 'close', 'vloume')

        permissions = (
            ("view_task", "Can see available tasks"),
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        )


class PostStockSerializer(serializers.ModelSerializer):
    stock = StockSerializer()

    class Meta:
        model = Stock

        # fields = '__all__'

class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ('file', 'userId')
