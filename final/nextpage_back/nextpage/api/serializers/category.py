# noinspection PyUnresolvedReferences
from api.models.category import Category
from rest_framework import serializers

class CategorySerializer1(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    

class CategorySerializer2(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Category
        fields = ('id', 'name')
    def get_name(self):
        return self.name