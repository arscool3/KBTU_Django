from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect, HttpResponseForbidden

def staff_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return _wrapped_view