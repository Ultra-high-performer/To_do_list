from django.urls import path
from home_page import views

urlpatterns = [
    path('', views.home_page , name = 'home'),
    path('add_todo' , views.add_todo , name = 'add_todo'),
    path('delete_todo/<int:todo_id>/' , views.delete_todo , name = 'delete_todo')

]
