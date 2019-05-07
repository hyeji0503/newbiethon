from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Review, Review2, Review3
import pdb

def category(request):
    return render(request, 'category.html')
    
def home(request):
    return render(request, 'home.html')
    
def univ(request):
    return render(request, 'univ.html')
    
def map_clothes(request):
    return render(request, 'map_clothes.html')

def map_drinks(request):
    return render(request, 'map_drinks.html')
    
def map_food(request):
    return render(request, 'map_food.html')
    
def list(request):
    review = Review.objects.all()
    return render(request, 'list.html', {'review': review})
    
    
def list2(request):
    review2 = Review2.objects.all()
    return render(request, 'list2.html', {'review2': review2})
    

def list3(request):
    review3 = Review3.objects.all()
    return render(request, 'list3.html', {'review3': review3})
    
    
def review(request):
    if request.method == "POST":
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        description = request.POST.get('description')
        is_like = request.POST.get('is_like')
        review = Review(title=title, writer=writer, description=description, radio=is_like)
        review.save()
        return redirect('list')
    return render(request, 'review.html')


def review2(request):
    if request.method == "POST":
        title2 = request.POST.get('title2')
        writer2 = request.POST.get('writer2')
        description2 = request.POST.get('description2')
        is_like2 = request.POST.get('is_like2')
        review2 = Review2(title2=title2, writer2=writer2, description2=description2, radio2=is_like2)
        review2.save()
        return redirect('list2')
    return render(request, 'review2.html')
    

def review3(request):
    if request.method == "POST":
        title3 = request.POST.get('title3')
        writer3 = request.POST.get('writer3')
        description3 = request.POST.get('description3')
        is_like3 = request.POST.get('is_like3')
        review3 = Review3(title3=title3, writer3=writer3, description3=description3, radio3=is_like3)
        review3.save()
        return redirect('list3')
    return render(request, 'review3.html')
    

def show(request, id):
    review = Review.objects.get(pk=id)
    return render(request, 'show.html', {'review':review})
    
    
def show2(request, id):
    review2 = Review2.objects.get(pk=id)
    return render(request, 'show2.html', {'review2':review2})
    
    
def show3(request, id):
    review3 = Review3.objects.get(pk=id)
    return render(request, 'show3.html', {'review3':review3})    
    
    
def edit(request, id):
    review = Review.objects.get(pk=id)
    return render(request, 'edit.html', {'review': review})
    
    
def edit2(request, id):
    review2 = Review2.objects.get(pk=id)
    return render(request, 'edit2.html', {'review2': review2})
    
    
def edit3(request, id):
    review3 = Review3.objects.get(pk=id)
    return render(request, 'edit3.html', {'review3': review3})
    
    
def update(request, id):
    if request.method=="POST":
        review = Review.objects.get(pk=id)
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        description = request.POST.get('description')
        review.title = title
        review.writer = writer
        review.description = description
        # print(review.radio)

        review.radio='dislike' if request.POST.get('is_like')=='dislike' else 'like'
        # print(review.radio)
        # review.like = request.POST.get('is_like')
        review.save()
        return redirect('show', review.pk)
        

def update2(request, id):
    if request.method=="POST":
        review2 = Review2.objects.get(pk=id)
        title2 = request.POST.get('title2')
        writer2 = request.POST.get('writer2')
        description2 = request.POST.get('description2')
        review2.title2 = title2
        review2.writer2 = writer2
        review2.description2 = description2
        review2.radio2='dislike' if request.POST.get('is_like')=='dislike' else 'like'
        review2.save()
        return redirect('show2', review2.pk)
        
def update3(request, id):
    if request.method=="POST":
        review3 = Review3.objects.get(pk=id)
        title3 = request.POST.get('title3')
        writer3 = request.POST.get('writer3')
        description3 = request.POST.get('description3')
        review3.title3 = title3
        review3.writer3 = writer3
        review3.description3 = description3
        review3.radio3='dislike' if request.POST.get('is_like')=='dislike' else 'like'
        review3.save()
        return redirect('show3', review3.pk)


def delete(request, id):
    if request.method == "POST":
        review = Review.objects.get(pk=id)
        review.delete()
        return redirect('list')
        
        
def delete2(request, id):
    if request.method == "POST":
        review2 = Review2.objects.get(pk=id)
        review2.delete()
        return redirect('list2')
        
        
def delete3(request, id):
    if request.method == "POST":
        review3 = Review3.objects.get(pk=id)
        review3.delete()
        return redirect('list3')