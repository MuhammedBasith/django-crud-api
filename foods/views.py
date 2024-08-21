from django.http import JsonResponse
from .models import Food
from .serializers import FoodSerializer


def get_food_list(request):
    foods = Food.objects.all()
    serializer = FoodSerializer(foods, many=True)
    return JsonResponse({'foods': serializer.data})
