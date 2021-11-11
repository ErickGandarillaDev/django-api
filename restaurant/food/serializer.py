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
        fields = ( 'id','name','address','phone')

class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Purchase
        fields = '__all__'


class DishSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Dish
        fields = '__all__'

class DetaildishSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Detaildish
        fields = '__all__'