from rest_framework import permissions


class IsSellerOrReady(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        
        return request.user.is_authenticated and request.user.is_seller


class IsOwnerOrReady(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        
        if request.user.is_authenticated and request.user.is_seller:
                return request.user.id == obj.seller.id
            
        return False

