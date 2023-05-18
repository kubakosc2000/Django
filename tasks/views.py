from django.shortcuts import render, get_object_or_404, redirect
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_add(request):
    if request.method == 'POST':
        # Pobierz dane z formularza
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        completed = False
        task_type = request.POST.get('task_type')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Utwórz nowe zadanie
        task = Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            completed=completed,
            task_type=task_type,
            phone=phone,
            email=email
        )

        return redirect('task_list')

    return render(request, 'tasks/task_add.html', {'task_type': None})


def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        # Pobierz dane z formularza
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.completed = False
        task.task_type = request.POST.get('task_type')
        task.phone = request.POST.get('phone')
        task.email = request.POST.get('email')

        task.save()
        return redirect('task_list')

    return render(request, 'tasks/task_edit.html', {'task': task})

def task_remove(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def task_toggle_completion(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
