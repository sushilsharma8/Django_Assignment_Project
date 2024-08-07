from django.contrib import messages
from django.shortcuts import redirect
from functools import wraps
from django.http import HttpResponseForbidden

def role_required(*roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.role in roles:
                return view_func(request, *args, **kwargs)
            else:
                messages.warning(request, "Permission Denied: You do not have the required role to access this page.")
                return redirect('permission_denied')  # Redirect to a custom permission denied page
        return _wrapped_view
    return decorator
