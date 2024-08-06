# myapp/forms.py
from django import forms
from django.contrib.auth import authenticate
from .models import Assignment
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'role', 'student_id', 'teacher_id']

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        student_id = cleaned_data.get('student_id')
        teacher_id = cleaned_data.get('teacher_id')

        if role == CustomUser.STUDENT and not student_id:
            self.add_error('student_id', 'Student ID is required for students.')
        elif role == CustomUser.TEACHER and not teacher_id:
            self.add_error('teacher_id', 'Teacher ID is required for teachers.')
        elif role == CustomUser.PRINCIPAL and (student_id or teacher_id):
            self.add_error('role', 'Principal should not have a student or teacher ID.')

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError('Invalid username or password')
            if not user.is_active:
                raise forms.ValidationError('This account is inactive.')

        return cleaned_data

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['student_id', 'title', 'description']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['grade', 'feedback']
        widgets = {
            'grade': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',  # Minimum value
                'max': '10',  # Maximum value
                'step': '1'  # Step value
            }),
            'feedback': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'grade': 'Grade',
            'feedback': 'Feedback',
        }
    
    # Add validators for the grade field
    grade = forms.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }