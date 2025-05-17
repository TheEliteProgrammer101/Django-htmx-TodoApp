
from django.http import HttpResponse
from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    context = {"tasks":tasks}
    return render(request, "todo_list.html", context)

def task_create(request):
    if request.POST.get("task_id"):
        task_id = request.POST.get("task_id")
        task = Task.objects.get(id=task_id)
        task.title = request.POST.get("task")
        task.save()
    else:
        task_name = request.POST.get("task")
        task = Task.objects.create(title=task_name)
    tasks = Task.objects.all()
    context = {"tasks":tasks}
    return render(request, "todo_list.html", context)


def task_append(request, pk):
    task = Task.objects.get(id=pk)
    print(task.title)
    return HttpResponse(f'''
<input type="hidden" value="{task.id}"name="task_id">         
<input type="text" value="{task.title}" placeholder="Enter Todo" name="task" id="input" required/>
                        ''')

def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    tasks = Task.objects.all()
    task.delete()
    context = {'tasks': tasks}
    return render(request, "todo_list.html", context)

def task_completed(request, pk):
    task = Task.objects.get(id=pk)
    if task.completed == False:
        task.completed = True
    else:
        task.completed = False
    task.save()
    tasks = Task.objects.all()
    context = {"tasks":tasks}
    return render(request, "todo_list.html", context)