from rest_framework import serializers
from demo.models import Item


class ItemSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price']