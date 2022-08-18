from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated


from vacantes.models import Vacante
from company.models import Empresa
from intereses.models import Area
from users.models import User
from members.models import Persona
from vacantes.serializers import VacantesSerializer, JobsListSerializer, CompanyJobListSerializer

from vacantes.permissions import IsCompany

# Create your views here.
class CreateVacanteView(APIView):
	permission_classes = [IsAuthenticated, IsCompany]
	
	def post(self, request):
		data = request.data 
		serializer = VacantesSerializer(data=data)
		user = request.data.get('company', '')
		if Empresa.objects.filter(user=user).exists():
			if serializer.is_valid(raise_exception=True):
				serializer.save()
				return Response({'status': 201, 
									'message': 'Una nueva vacante ha sido creada', 
									'data': serializer.data})
			return Response({'status':400, 'message':'Algo no esta bien con tus datos ingresados'})
		return Response({'status': 400, 'message':'Este usuario no tiene un perfil de empresa, necesitas crearlo primero'})


# vista de cada vacante
class DetailVacanteView(APIView):
	permission_classes = [IsAuthenticated]
	def get(self, request, vacante_id):
		vacante = get_object_or_404(Vacante, pk=vacante_id)
		serializer = JobsListSerializer(vacante)
		return Response({'status':200, 'message':'Detalle de vacante', 'data':serializer.data})

	def put(self, request, vacante_id):
		vacante = get_object_or_404(Vacante, pk=vacante_id)
		serializer = VacantesSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response({'status':206, 
				'message':'vacante actualizada correctamente', 
				'data':serializer.data })
		return Response({'status':400, 'message':'algo no esta bien con la informacion que has ingresado'})

# lista de busqueda de vacantes *****
class SearchView(APIView):
	permission_classes = [IsAuthenticated]

	def get (self, request, *args, **kwargs):
		vacantes = Vacante.objects.all()
		a = self.request.query_params.get('area',None)
		j = self.request.query_params.get('jobrole',None)
		i = self.request.query_params.get('company__is_approved',None)
		s = self.request.query_params.get('search', None)

		if a:
			vacantes=vacantes.filter(area=a)
		if j:
			vacantes=vacantes.filter(jobrole=j)
		if i:
			vacantes=vacantes.filter(company__is_approved=i)
		if s:
			vacantes=vacantes.filter(descripcion__icontains=s)
		
		serializer = JobsListSerializer(vacantes, many=True)
		return Response({'status':200, 
			'message':'Lista de busqueda de vacantes', 
			'data':serializer.data})




#Todas las vacantes por empresa
class CompanyJobsListView(APIView):
	permission_classes = [IsAuthenticated]
	
	def get(self, request):
		if Empresa.objects.filter(user=request.user).exists():
			company = Empresa.objects.get(user=request.user)
			vacantes = Vacante.objects.filter(company=company)
			serializer = CompanyJobListSerializer(vacantes, many=True)
			return Response({'status':200, 'message': 'Lista de vacantes por empresa', 'data':serializer.data})
		return Response({'status':404, 'message':'esta usuario no tiene un perfil de empresa'})

# lista de vacantes de empresa por area
class CompanyAreaJobsListView(APIView):
	permission_classes = [IsAuthenticated]
	
	def get(self, request, area_id):
		company = Empresa.objects.get(user=request.user)
		vacantes = Vacante.objects.filter(company=company, area=area_id)
		serializer = CompanyJobListSerializer(vacantes, many=True)
		return Response({'status':200, 'message': 'Lista de vacantes empresa por area', 'data':serializer.data})

# lista de vacantes de empresa por tipo de trabajo
class CompanyTipoJobsListView(APIView):
	permission_classes = [IsAuthenticated]
	
	def get(self, request, tipo_trabajo_id):
		company = Empresa.objects.get(user=request.user)
		vacantes = Vacante.objects.filter(company=company, tipo_trabajo=tipo_trabajo_id)
		serializer = CompanyJobListSerializer(vacantes, many=True)
		return Response({'status':200, 'message': 'Lista de vacantes empresa por tipo de trabajo', 'data':serializer.data})

# lista de vacantes de empresa por modalidad
class CompanyModJobsListView(APIView):
	permission_classes = [IsAuthenticated]
	
	def get(self, request, modalidad_id):
		company = Empresa.objects.get(user=request.user)
		vacantes = Vacante.objects.filter(company=company, modalidad=modalidad_id)
		serializer = CompanyJobListSerializer(vacantes, many=True)
		return Response({'status':200, 'message': 'Lista de vacantes empresa por modalidad', 'data':serializer.data})











