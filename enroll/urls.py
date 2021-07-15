from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name="index"),
    path('delete/<str:pk>' , views.delete , name="delete"),
    path('<str:pk>' , views.edit , name="edit")
]