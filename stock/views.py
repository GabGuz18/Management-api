from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import *
from .models import *
from .helpers import (
    checkQuantity
)
from .errorHandlers import *

# Create your views here.
class ProductsViewSet(viewsets.ViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        try:

            data = Products.objects.all()

            return Response(
                {'error': 'false', 'message':f'Data: {data}'},
                status=status.HTTP_200_OK
            )
        
        except Exception as err:
            return Response(
                {'error': 'true', 'message':'Something went wrong in order to fetch data'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def create(self, request):
        try:
            data = request.data
            name = data['product']
            category = data['category']

            categories = Categories.objects.get(id=category)
            data['category'] = categories

            product = Products.objects.create(**data)

            return Response(
                {'error': 'false', 'message':f'Product created: {name}'},
                status=status.HTTP_201_CREATED
            )
        except Exception as err:
            print(err)
            return Response(
                {'error': 'true', 'message':f'error: {err}'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def update(self, request, pk=None):
        try:
            data = request.data
            category = data['category']

            categories = Categories.objects.get(id=category)
            data['category'] = categories

            product = Products.objects.filter(id=pk).update(**data)

            return Response(
                {'error': 'false', 'message':f'Product created: {data}'},
                status=status.HTTP_201_CREATED
            )
        
        except Exception as err:
            return Response(
                {'error': 'true', 'message':f'error: {err}'},
                status=status.HTTP_400_BAD_REQUEST
            )


class IngredientsViewSet(viewsets.ViewSet):
    serializer_class = IngredientsSerializer
    queryset = Ingredients.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        try:

            data = Ingredients.objects.all()

            return Response(
                {'error': 'false', 'message':f'Data: {data}'},
                status=status.HTTP_200_OK
            )
        
        except Exception as err:
            return Response(
                {'error': 'true', 'message':'Something went wrong in order to fetch data'},
                status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request):
        try:
            data = request.data
            name = data['ingredient']
            product = data['product']

            products = Products.objects.get(product=product)
            data['product'] = products

            if Ingredients.objects.filter(ingredient=name, product=products).exists():
                raise IngredientDuplicatedError('Ingredient duplicated')

            Ingredients.objects.create(**data)

            min_quantity = checkQuantity(product)

            return Response(
                {'error': 'false', 'message':f'Ingredient created: {name}; Product quantity: {min_quantity}'},
                status=status.HTTP_201_CREATED
            )
        except Exception as err:
            print(err)
            return Response(
                {'error': 'true', 'message':f'error: {err}'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def update(self, request, pk=None):
        try:
            data = request.data
            product = data['product']

            products = Products.objects.get(product=product)
            data['product'] = products

            Ingredients.objects.filter(id=pk).update(**data)

            return Response(
                {'error': 'false', 'message':f'Product created: {data}'},
                status=status.HTTP_201_CREATED
            )
        
        except Exception as err:
            return Response(
                {'error': 'true', 'message':f'error: {err}'},
                status=status.HTTP_400_BAD_REQUEST
            )
        

