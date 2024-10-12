from django.urls import path
from task_manager.labels import views


urlpatterns = [
    path('', views.LabelsListView.as_view(),
         name="labels"),
    path('create/', views.LabelCreateView.as_view(),
         name="label_create"),
]
