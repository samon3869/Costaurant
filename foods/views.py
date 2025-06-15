from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    today = datetime.now().date()
    context = {
        'date': today,
    }
    return render(request, 'foods/index.html', context=context)

def food_detail(request, food):
    context = {
        'food': food,
    }
    return render(request, 'foods/foods.html', context=context)