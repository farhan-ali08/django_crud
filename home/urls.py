from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('showdata', views.showdata, name='showdata'),
    path('editdata/<int:id>', views.editdata, name='editdata'),
    path('updatedata/<int:id>', views.updatedata, name='update'),
    path('delete/<int:id>', views.delete, name="delete")
]
