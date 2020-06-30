from django.shortcuts import render
from home_page.models import todo
from django.utils import timezone

from django.http import HttpResponseRedirect
# Create your views here.

def home_page(request):
    todo_items = todo.objects.all().order_by("-added_date")
    return render(request , 'home.html' , {'todo_items' :todo_items})

def add_todo(request):
    current_date = timezone.now()
    content = request.POST['content']


    todo.objects.create(added_date = current_date , text = content)

    # todo_items = todo.objects.all().order_by("-added_date")
    # return render(request , 'home.html' , {'todo_items' : todo_items})
    return HttpResponseRedirect('/')

    

def delete_todo(request , todo_id):

    todo.objects.get(id = todo_id).delete()

    # todo_items = todo.objects.all().order_by("-added_date")
    # return render(request , 'home.html' , {'todo_items' : todo_items})
    return HttpResponseRedirect('/')

