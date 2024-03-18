from rest_framework import serializers
from . import models


class RankerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ranker
        fields = ['user', 'full_name', 'facebook', 'image', 'vote']
