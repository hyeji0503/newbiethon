from django.shortcuts import render, redirect
from .models import Review
import pd

def category(request):
    return render(request, 'category.html')
    
def home(request):
    return render(request, 'home.html')
    
def map_clothes(request):
    return render(request, 'map_clothes.html')

def map_drinks(request):
    return render(request, 'map_drinks.html')
    
def map_food(request):
    return render(request, 'map_food.html')
    
def list(request):
    review = Review.objects.all()
    return render(request, 'list.html', {'review': review})
    
def review(request):
    if request.method == "POST
        pdb.set_trace()
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        description = request.POST.get('description')
        radio = request.POST.get('radio')
        review = Review(title=title, writer=writer, description=description)
        review.save()
        return redirect('list')
    return render(request, 'review.html')