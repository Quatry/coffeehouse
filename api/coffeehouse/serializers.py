from rest_framework import serializers

from api.models import CoffeeHouse


class CoffeeHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeHouse
        fields = '__all__'
