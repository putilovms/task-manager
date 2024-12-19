from django.contrib import admin
from django.urls import include, path
from task_manager import views

handler404 = 'task_manager.views.page404'
handler500 = 'task_manager.views.page500'

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('labels/', include('task_manager.labels.urls')),
]
