# myapp/views.py
from django.http import JsonResponse
from .forms import AssignmentForm, RegistrationForm, GradeForm
from .models import Assignment, CustomUser
from .forms import CustomUserForm
from .serializers import AssignmentSerializer
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from .decorators import role_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django import forms
from django.shortcuts import get_object_or_404
from django.contrib import messages
import logging

# Get an instance of a logger
logger = logging.getLogger('myapp')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def list_assignments(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignments.html', {'assignments': assignments})

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Assignment added successfully!')
            return redirect('list_assignments')
    else:
        form = AssignmentForm()
    return render(request, 'add_assignment.html', {'form': form})

@login_required
def update_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Assignment updated successfully!')
            return redirect('list_assignments')
    else:
        form = AssignmentForm(instance=assignment)
    return render(request, 'update_assignment.html', {'form': form})

@login_required
def delete_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == 'POST':
        assignment.delete()
        messages.success(request, 'Assignment deleted successfully!')
        return redirect('list_assignments')
    return render(request, 'delete_assignment.html', {'assignment': assignment})

@login_required
@role_required('teacher')
# @permission_required('teacher')
def grade_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    # if request.user.role != 'Teacher':
    #     return redirect('list_assignments')
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Assignment graded successfully!')
            return redirect('list_assignments')
    else:
        form = GradeForm(instance=assignment)
    return render(request, 'grade_assignment.html', {'form': form, 'assignment': assignment})

@login_required
@role_required('principal')
def manage_users(request):
    users = CustomUser.objects.all()
    return render(request, 'manage_users.html', {'users': users})

@login_required
@role_required('principal')
def add_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User added successfully!')
            return redirect('manage_users')
    else:
        form = CustomUserForm()
    return render(request, 'add_user.html', {'form': form})

@login_required
@role_required('principal')
def update_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully!')
            return redirect('manage_users')
    else:
        form = CustomUserForm(instance=user)
    return render(request, 'update_user.html', {'form': form})

@login_required
@role_required('principal')
def delete_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully!')
        return redirect('manage_users')
    return render(request, 'delete_user.html', {'user': user})