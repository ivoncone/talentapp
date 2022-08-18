from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsCompany(BasePermission):
	message = 'Crear vacantes es un permiso de empresa'


	def has_object_permission(self, request, view, obj):

		if request.method in SAFE_METHODS:
			return True

		return obj.empresa == request.user