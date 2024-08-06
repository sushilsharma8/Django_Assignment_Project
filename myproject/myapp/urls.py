from django.urls import path
from . import views

urlpatterns = [
    path('assignments/', views.list_assignments, name='list_assignments'),
    path('assignments/add/', views.add_assignment, name='add_assignment'),
    path('assignments/update/<int:pk>/', views.update_assignment, name='update_assignment'),
    path('assignments/delete/<int:pk>/', views.delete_assignment, name='delete_assignment'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('grade_assignment/<int:pk>/', views.grade_assignment, name='grade_assignment'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('add_user/', views.add_user, name='add_user'),
    path('update_user/<int:pk>/', views.update_user, name='update_user'),
    path('delete_user/<int:pk>/', views.delete_user, name='delete_user'),
    path('logout/', views.logout_view, name='logout'),
    # path('base/', views.home, name='base'),
]