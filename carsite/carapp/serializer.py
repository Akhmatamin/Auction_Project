from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username','email','password','first_name','last_name',
                  'phone_number','role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect username or password")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user' : {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['car_image']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['brand']

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['model']

class AuctionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ['end_time',]

class CarListSerializer(serializers.ModelSerializer):
    car_images = CarImageSerializer(many=True,read_only=True)
    brand = BrandSerializer()
    model = ModelSerializer()
    auction = AuctionListSerializer(many=True,read_only=True)
    class Meta:
        model = Car
        fields = ['model','brand','year','country','car_images','transmission_type','mileage',
                  'fuel_type','price','car_status','auction']

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'

class AuctionSerializer(serializers.ModelSerializer):
    bid = BidSerializer(many=True,read_only=True)
    class Meta:
        model = Auction
        fields = ['car','start_price','min_price','start_time','end_time',
                  'status','bid']

class FeedbackSerializer(serializers.ModelSerializer):
    seller = serializers.CharField(source='seller.username', read_only=True)
    buyer = serializers.CharField(source='buyer.username', read_only=True)

    class Meta:
        model = Feedback
        fields = ['seller','buyer','rating','comment','created_at']

class CarDetailSerializer(serializers.ModelSerializer):
    car_images = CarImageSerializer(many=True,read_only=True)
    brand = BrandSerializer()
    model = ModelSerializer()
    auction = AuctionSerializer(many=True)
    car_feedback = FeedbackSerializer(many=True,read_only=True)
    class Meta:
        model = Car
        fields = ['model', 'brand', 'year', 'country', 'car_images', 'transmission_type', 'mileage',
                  'fuel_type', 'price', 'car_status','description','color','power','damages',
                  'address', 'auction','car_feedback']




