from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('department/<int:dept_id>/follow/', views.follow_department, name='follow_department'),
    path('department/<int:dept_id>/unfollow/', views.unfollow_department, name='unfollow_department'),
    path('join-event/<int:event_id>/', views.join_event, name='join_event'),
    path('events/<int:event_id>/leave/', views.leave_event, name='leave_event'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage-department/', views.manage_department, name='manage_department'), 
    path('add-department/', views.add_department, name='add_department'),
    path('edit-department/<int:department_id>/', views.edit_department, name='edit_department'),
    path('delete-department/<int:department_id>/', views.delete_department, name='delete_department'),
    path('add-event/', views.add_event, name='add_event'),
    path('edit-event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete-event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('add-news/', views.add_news, name='add_news'),
    path('edit-news/<int:item_id>/', views.edit_news, name='edit_news'),
    path('delete-news/<int:item_id>/', views.delete_news, name='delete_news'),
    path('upload-news/', views.upload_news, name='upload_news'),
    path('departments/', views.department_overview, name='department_overview'),
    path('events/', views.event_list, name='event_list'),
]
