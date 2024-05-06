from rest_framework import serializers
from .models import CosmeticProduct

class CosmeticProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CosmeticProduct
        fields = '__all__'
