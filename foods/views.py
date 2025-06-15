from django.shortcuts import render
from datetime import datetime
from django.http import Http404
from foods.models import Menu

# Create your views here.
def index(request):
    context = dict()
    today = datetime.now().date()
    menus = Menu.objects.all()
    context['date'] = today
    context['menus'] = menus
    return render(request, 'foods/index.html', context=context)

def food_detail(request, food):
    context = dict()
    if food == "chicken" :
        context['name'] = "Chicken"
        context['description'] = "A delicious chicken dish."
        context['price'] = 10.99
        context['img_url'] = "foods/images/chicken.jpg"
    elif food == "burger":
        context['name'] = "Burger"
        context['description'] = "A juicy burger with all the fixings."
        context['price'] = 8.99
        context['img_url'] = "foods/images/burger.jpg"
    # elif food == "pizza":
    #     context['name'] = "Pizza"
    #     context['description'] = "A tasty pizza with fresh ingredients."
    #     context['price'] = 12.99
    #     context['img_url'] = "foods/images/pizza.jpg"
    # else:           
    #     context['name'] = "Unknown Food"
    #     context['description'] = "No description available."
    #     context['price'] = 0.00
    #     context['img_url'] = "foods/images/unknown.jpg"
    else :
        raise Http404("Food not found")
    return render(request, 'foods/foods.html', context=context)