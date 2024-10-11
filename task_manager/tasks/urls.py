from django.urls import path
from task_manager.tasks import views


urlpatterns = [
    path('', views.TasksListView.as_view(),
         name="tasks"),
    path('create/', views.TasksCreateView.as_view(),
         name="task_create"),
    path('<int:pk>/delete/', views.TasksDeleteView.as_view(),
         name="task_delete"),
    path('<int:pk>/update/', views.TasksUpdateView.as_view(),
         name="task_update"),
    path('<int:pk>/', views.TaskView.as_view(),
         name="task"),
]
