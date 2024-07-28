from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('assignments/', views.list_assignments, name='list_assignments'),
    path('assignments/add/', views.add_assignment, name='add_assignment'),
    path('assignments/update/<int:pk>/', views.update_assignment, name='update_assignment'),
    path('assignments/delete/<int:pk>/', views.delete_assignment, name='delete_assignment'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
]