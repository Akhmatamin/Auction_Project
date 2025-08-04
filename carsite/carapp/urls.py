from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user',UserProfileViewSet, basename='users')
router.register(r'brand',BrandViewSet, basename='brands')
router.register(r'model',ModelViewSet, basename='models')
router.register(r'auction',AuctionViewSet, basename='auctions')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('car/',CarListAPIView.as_view(), name='car-list'),
    path('car/<int:pk>/', CarDetailAPIView.as_view(), name='car-detail'),
    path('feedback/',FeedbackAPIView.as_view(), name='feedback'),
    path('car/create',CarCreateAPIView.as_view(), name='car-create'),
    path('car/edit',CarEditAPIView.as_view(), name='car-edit'),
    path('bids/',BidAPIView.as_view(), name='bids'),

]