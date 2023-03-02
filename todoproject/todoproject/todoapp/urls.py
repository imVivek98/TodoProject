from . import views
from django.urls import path

urlpatterns = [
    path('',views.home_pg,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.todoListView.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.todoDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.taskUpdate.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.taskDelete.as_view(),name='cbvdelete'),
]