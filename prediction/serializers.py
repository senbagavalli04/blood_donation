# prediction/serializers.py
from rest_framework import serializers
class PredictionSerializer(serializers.Serializer):
    recency = serializers.FloatField()
    frequency = serializers.FloatField()
    monetary = serializers.FloatField()
    time = serializers.FloatField()
