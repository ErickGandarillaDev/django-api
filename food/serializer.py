from rest_framework import serializers
from .models import Purchase
from .models import Dish
from .models import Detaildish
from .models import Restaurant
# Create a model serializer 
class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Restaurant
        fields = ('url', 'id','name','address','phone')

class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Purchase
        fields = ('url', 'id', 'date', 'identification','payment','service','restaurant_id')

class DishSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Dish
        fields = ('url', 'id','purchase_id')

class DetaildishSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Detaildish
        fields = ('url', 'id', 'name','size','price','dish_id')