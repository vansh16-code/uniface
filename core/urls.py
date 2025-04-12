from django.urls import path
from . import views
from .views import register,upload_news

urlpatterns = [
    path('', views.home, name='home'),
    path('follow/<int:dept_id>/', views.follow_department, name='follow_department'),
    path('unfollow/<int:dept_id>/', views.unfollow_department, name='unfollow_department'),
    path('add-event/', views.add_event, name='add_event'),
    path('register/', register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('join-event/<int:event_id>/', views.join_event, name='join_event'),
    path('events/<int:event_id>/leave/', views.leave_event, name='leave_event'),
    path('department/<int:dept_id>/follow/', views.follow_department, name='follow_department'),
    path('department/<int:dept_id>/unfollow/', views.unfollow_department, name='unfollow_department'),
    path('upload-news/', upload_news, name='upload_news'),
    path('departments/', views.department_overview, name='department_overview'),
    path('events/', views.event_list, name='event_list'),
    path('upload_news/', views.upload_news, name='upload_news'),

]
