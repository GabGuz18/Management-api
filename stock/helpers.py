from .models import *
from .errorHandlers import *

def checkQuantity(name):
    try:
        product = Products.objects.get(product=name)
        ingredients = list(Ingredients.objects.filter(product=product).values())

        quantities = []
        for ingredient in ingredients:
            quantities.append(ingredient['quantity'])
        
        min_quantity = min(quantities)
        Products.objects.filter(product=name).update(quantity=min_quantity)

        return min_quantity

    except Exception as err:
        UpdateQuantityError('Error at update quantity')
