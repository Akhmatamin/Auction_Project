from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator,MaxValueValidator

class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('buyer', 'buyer'),
        ('seller', 'seller'),
    )
    role = models.CharField(choices=ROLE_CHOICES, default='buyer')
    phone_number = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return self.username

class Country(models.Model):
    country_name = models.CharField(max_length=50, unique=True)
    country_image = models.ImageField(upload_to='country_images/')

    def __str__(self):
        return self.country_name

class Car(models.Model):
    year = models.PositiveIntegerField()
    FUEL_TYPES = (
        ('electric', 'electric'),
        ('gas', 'gas'),
        ('diesel','diesel'),
        ('petrol','petrol'),
        ('hybrid','hybrid'),
    )
    fuel_type = models.CharField(choices=FUEL_TYPES, default='petrol')

    TRANSMISSION_TYPES = (
        ('manual', 'manual'),
        ('automatic', 'automatic'),
        ('robot', 'robot'),
        ('CVT','CVT')
    )
    transmission_type = models.CharField(choices=TRANSMISSION_TYPES, default='automatic')
    mileage = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    description = models.TextField()
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    address = models.TextField()
    color = models.CharField(max_length=32)
    power = models.PositiveSmallIntegerField()
    damages = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'{self.seller} - {self.year}'

class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    car_image = models.ImageField()

    def __str__(self):
        return self.car


class Brand(models.Model):
    brand = models.CharField(max_length=100)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.brand

class Model(models.Model):
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.model

class Auction(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_price = models.PositiveIntegerField()
    min_price = models.PositiveIntegerField(validators=[MinValueValidator(10)])
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    STATUS_CHOICES = (
        ('active', 'active'),
        ('finished', 'finished'),
        ('cancelled', 'cancelled'),
    )
    status = models.CharField(choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f'{self.car} - {self.status}'

class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(validators=[MinValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.buyer} - {self.amount}'

class Feedback(models.Model):
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i))for i in range(1,6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.seller} - {self.rating}'
