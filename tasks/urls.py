from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.task_add, name='task_add'),
    path('edit/<int:task_id>/', views.task_edit, name='task_edit'),
    path('tasks/remove/<int:task_id>', views.task_remove, name='task_remove'),
    path('tasks/toggle-completion/<int:task_id>', views.task_toggle_completion, name='task_toggle_completion')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
