from django.shortcuts import render
from .models import Food, Consume

# Create your views here.
def index(request):
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, consumed_food=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()
    consumed_by_user = Consume.objects.filter(user = request.user)
    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_by_user': consumed_by_user})