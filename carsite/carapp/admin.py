from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import *


class CarImage(TabularInline):
    model = CarImage
    extra = 1

class ModelCar(TabularInline):
    model = Model
    extra = 1

class BrandCar(TabularInline):
    model = Brand
    extra = 1

class BidsCar(TabularInline):
    model = Bid
    extra = 1

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [CarImage,BrandCar]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    inlines = [ModelCar]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    inlines = [BidsCar]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Country)
admin.site.register(Feedback)


