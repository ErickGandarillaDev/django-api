# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers  
# import everything from views
from .views import *
  
# define the router
router = routers.DefaultRouter()
  
# define the router path and viewset to be used
router.register(r'restaurant', RestaurantViewSet)
router.register(r'purchase', PurchaseViewSet)
router.register(r'dish', DishViewSet)
router.register(r'detaildish', DetaildishViewSet)

  
# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
]
