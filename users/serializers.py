from rest_framework import serializers

from django.contrib.auth.hashers import make_password , check_password
from django.utils.crypto import get_random_string
from django.core.validators import MinLengthValidator
from django.core.mail import send_mail
from django.conf import settings



from random import randint

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
class SignUPSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required = True)
    email = serializers.CharField(required = True)
    password = serializers.CharField(write_only = True , validators=[MinLengthValidator(8)] , required = True)
    confirm_password = serializers.CharField(required = True , write_only = True)
    # user_type = serializers.ChoiceField(choices=User.UserType.choices , required = True)
    class Meta:
        model = User
        fields = ('email','username','password','confirm_password','user_type')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"message":"password do not exist"})
        
        email_user = User.objects.filter(email = attrs['email']).first()
        
        if email_user:
            raise serializers.ValidationError({"message":"email is exist"})
        
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data["is_active"] = False
        validated_data['code'] = randint(1000,9999)
        user = User.objects.create_user(**validated_data)

        send_mail(
            f"Activation Code ",
            f"welcome {validated_data['username']}\n Here is the activation code : {validated_data['code']}.",
            settings.EMAIL_HOST_USER,
            {validated_data['email']},
            fail_silently=False,
        )
        return {}
    
    def to_representation(self, instance):
        return {'message': 'chick your gmail.'}

class ActivateSerializer(serializers.Serializer):
    code = serializers.CharField(required = True)

    def create(self, validated_data):
        user_id = self.context['view'].kwargs['pk']
        user = User.objects.get(id = user_id)

        if user.code != validated_data['code']:
            raise serializers.ValidationError({'message':'code is not correct'})
        
        user.is_active = True
        user.code = ''
        user.save()
        
        return {}







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