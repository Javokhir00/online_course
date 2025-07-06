from django.shortcuts import redirect
from django.contrib.auth import logout
from django.utils.timezone import now
from config.settings import SESSION_COOKIE_AGE




class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        # Log the request details
        print(f"Request Method: {request.method}, Request Path: {request.path}")
        # Call the next middleware or view
        response = self.get_response(request)
        return response



class TimeLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            if last_activity:
                difference_time = (now()-now().fromisoformat(last_activity)).total_seconds()
                if difference_time > SESSION_COOKIE_AGE:
                    logout(request)
                    return redirect('shop:index')
            request.session['last_activity'] = now().isoformat()

        response = self.get_response(request)
        return response