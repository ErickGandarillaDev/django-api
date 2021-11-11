from rest_framework import viewsets
  
# import local data
from .serializer import PurchaseSerializer
from .serializer import DishSerializer
from .serializer import DetaildishSerializer
from .serializer import RestaurantSerializer
from .models import Purchase
from .models import Dish
from .models import Detaildish
from .models import Restaurant

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    http_method_names = ['get', 'post', 'put']

  
# create a viewset
class PurchaseViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Purchase.objects.all()
      
    # specify serializer to be used
    serializer_class = PurchaseSerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class DetaildishViewSet(viewsets.ModelViewSet):
    queryset = Detaildish.objects.all()
    serializer_class = DetaildishSerializer

