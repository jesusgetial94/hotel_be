from rest_framework import serializers
from authApp.models.user import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'identification', 'phone', 'email']
    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
                'id'                : user.id,
                'username'          : user.username,
                'name'              : user.name,
                'identification'    : user.identification,
                'phone'             : user.phone,
                'email'             : user.email,
        }