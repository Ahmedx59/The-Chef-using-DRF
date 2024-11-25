from django.contrib.auth.hashers import make_password , check_password
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'image',
            'date_joined',
        ]


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)
    
    def create(self, validated_data):#2024-11-25 18:34:26.152552+00:00

        user = self.context['request'].user

        if not check_password(validated_data['old_password'], user.password):
            raise serializers.ValidationError({'message':'old password not correct'})
        
        if validated_data['new_password'] != validated_data['confirm_new_password']:
            raise serializers.ValidationError({'message':'The New Passwords do not match.'})
        
        user.set_password(validated_data['new_password'])
        user.save()
        
        return {}
    
    def to_representation(self, instance):
        return {'message': 'Password change process completed.'}    