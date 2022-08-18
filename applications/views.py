from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from applications.models import Application
from members.models import Persona
from company.models import Empresa
from vacantes.models import Vacante

from applications.serializers import ApplicationSerializer, ApplicationCreateSerializer, ApplicationCompanySerializer

# lista de vacantes por persona que ha aplicado
class ApplicationListView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		persona = Persona.objects.get(user=request.user)
		a = Application.objects.filter(persona=persona)
		serializer = ApplicationSerializer(a, many=True)
		return Response({'status':200, 
			'message':'esta es la lista de vacantes a las que has aplicado', 
			'data':serializer.data})

# lista de todas las aplicaciones por empresa
class ApplicationCompanyView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request, *args, **kwargs):
		company = Empresa.objects.get(user=request.user)
		c = Application.objects.filter(vacante__company=company)
		# por vacante
		v = self.request.query_params.get('vacante', None)
		if v:
			c=c.filter(vacante=v)
		serializer = ApplicationCompanySerializer(c, many=True)
		return Response({'status':200, 
			'message':'esta son la lista de personas que han aplicado a tus vacantes',
			'data':serializer.data})




class ApplicationCreateView(APIView):
	permission_classes = [IsAuthenticated]

	def post(self, request):
		data = request.data
		serializer = ApplicationCreateSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response({'status':'201', 'message':'tu aplicacion ha sido recibida', 'data':serializer.data})
		return Response({'status':400, 'message':'algo no esta bien con tu informacion ingresada'})

