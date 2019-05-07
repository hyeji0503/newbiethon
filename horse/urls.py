from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('univ/', views.univ, name="univ"),
    path('category/', views.category, name="category"),
    path('map_clothes/', views.map_clothes, name="map_clothes"),
    path('map_drinks/', views.map_drinks, name="map_drinks"),
    path('map_food/', views.map_food, name="map_food"),
    path('review/', views.review, name="review"),
    path('review2/', views.review2, name="review2"),
    path('review3/', views.review3, name="review3"),
    path('list/', views.list, name="list"),
    path('list2/', views.list2, name="list2"),
    path('list3/', views.list3, name="list3"),
    path('show/<int:id>/', views.show, name="show"),
    path('show2/<int:id>/', views.show2, name="show2"),
    path('show3/<int:id>/', views.show3, name="show3"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('edit2/<int:id>/', views.edit2, name="edit2"),
    path('edit3/<int:id>/', views.edit3, name="edit3"),
    path('update/<int:id>/', views.update, name="update"),
    path('update2/<int:id>/', views.update2, name="update2"),
    path('update3/<int:id>/', views.update3, name="update3"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('delete2/<int:id>/', views.delete2, name="delete2"),
    path('delete3/<int:id>/', views.delete3, name="delete3"),
]