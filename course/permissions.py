from rest_framework import permissions
import datetime

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user



class CanJavohirRead(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.username == 'javohir':
            if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
                return False
            return True
        return True



class WeekDayOnlyAccess(permissions.BasePermission):
    def has_permission(self, request, view):
        today = datetime.datetime.today().weekday()
        return today != 0



class CanReadPremium(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff



class EvenYearsOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        year = datetime.now().year
        return year % 2 == 0



class SuperUserOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser



class PutAndPatchOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in ['PUT', 'PATCH']


