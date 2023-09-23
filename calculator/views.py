from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def get_recipe(request, dish):
    servings = request.GET.get('servings')
    dish = DATA[dish]
    print(servings)
    if servings:
        for key, value in dish.items():
            dish[key] = value * int(servings)
    context = {
        'recipe': dish
    }
    return render(request, 'calculator/index.html', context)


def hello(request):
    recipes_list = [dish + '\n' for dish in DATA.keys()]
    return HttpResponse(recipes_list)
