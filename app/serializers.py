from django.core.mail import send_mail
from django.conf import settings
from rest_framework import serializers
from .models import Kurs, Dars,Izoh,User,LikeBosish
from django_filters import rest_framework as filters

class KursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurs
        fields = '__all__'

class KursFilter(filters.FilterSet):
    class Meta:
        model = Kurs
        fields = ['name']

class DarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dars
        fields = '__all__'

class DarsFilter(filters.FilterSet):
    class Meta:
        model = Dars
        fields = ['name']
        
class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class EmailSerializer(serializers.Serializer):
    title = serializers.CharField()
    message = serializers.CharField()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeBosish
        fields = '__all__'
        

