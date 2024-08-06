from django.contrib import messages
from django.shortcuts import redirect
from functools import wraps
from django.http import HttpResponseForbidden

def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.role == role:
                return view_func(request, *args, **kwargs)
            else:
                messages.warning(request, "Permission Denied: You do not have the required role to access that page.")
                return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
