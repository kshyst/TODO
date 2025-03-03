from django.contrib.auth.models import User
from rest_framework import serializers

from Todo.models import Todo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url' , 'username' , 'email']


class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=128)
    checked = serializers.BooleanField(default=False)
    due_date = serializers.DateField(default="2000-01-01")

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id' , instance.id)
        instance.name = validated_data.get('name' , instance.name)
        instance.checked = validated_data.get('checked' , instance.checked)
        instance.due_date = validated_data.get('due_date' , instance.due_date)
        instance.save()
        return instance