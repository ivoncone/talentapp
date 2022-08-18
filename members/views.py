from django.shortcuts import render, redirect, get_object_or_404

from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from django.views.generic import DetailView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated


from members.models import Persona
from users.models import User 
from members.serializers import UserProfileSerializer, UserGeneralSerializer, UserSerializer, JobRoleListSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
import jwt 

# Create user view
class UserView(APIView):
	permission_classes = [IsAuthenticated, ]

	def get(self, request):
		user = User.objects.get(email=request.user)
		if Persona.objects.filter(user=user).exists():
			persona = Persona.objects.filter(user=user).first()
			serializer = UserProfileSerializer(persona)
			return Response({'status':200, 'data': serializer.data})
		return Response({'status':404, 'message': 'este solicitante no ha sido creado'})

# Create profile view
class ProfileCreate(APIView):
	permission_classes = [IsAuthenticated]
	
	def post(self, request):
		data = request.data
		serializer = UserGeneralSerializer(data=data)
		name = request.data.get('first_name', '')
		last = request.data.get('last_name', '')
		last_m = request.data.get('last_name_m', '')
		g = request.data.get('genero', '')
		birth = request.data.get('birth_date', '')
		civil = request.data.get('civil_status')
		age = request.data.get('age', '')
		state = request.data.get('state', '')
		city = request.data.get('residence', '')
		academico = request.data.get('datosAcademicos', '')
		area = request.data.get('area', '')
		job = request.data.get('jobrole', '')
		tipo = request.data.get('tipo_trabajo', '')
		modalid = request.data.get('modalidad', '')
		video = request.data.get('video', '')
		
		if name == '':
			return Response({'status':400, 'message': ' Ingresa tun nombre'})
		if last == '':
			return Response({'status':400, 'message': ' Ingresa tu apellido'})
		if last_m == '':
			return Response({'status':400, 'message': ' Ingresa tu segundo apellido'})
		if g == '':
			return Response({'status':400, 'message': ' Ingresa tu genero si no deseas ponerlo indica otro'})
		if birth == '':
			return Response({'status':400, 'message': ' Ingresa tu fecha de nacimiento'})
		if civil == '':
			return Response({'status':400, 'message': ' Ingresa tu estado civil o seleccion prefiero no responder'})
		if age == '':
			return Response({'status':400, 'message': ' Ingresa tu edad'})
		if state == '':
			return Response({'status':400, 'message': ' selecciona tu estado de residencia'})
		if city == '':
			return Response({'status':400, 'message': 'escribe la ciudad, municipio o localidad donde vives'})
		if academico == '':
			return Response({'status':400, 'message': 'escribe por lo menos un dato academico, puede ser un curso o taller que hayas tomado'})
		if area == '':
			return Response({'status':400, 'message': ' Ingresa el area de interes'})
		if job == '':
			return Response({'status':400, 'message': ' Ingresa el role de interes'})
		if tipo == '':
			return Response({'status':400, 'message': ' Ingresa tu preferencia de horario'})
		if modalid == '':
			return Response({'status':400, 'message': ' Ingresa tu prefencia remoto o presencial'})
		if video == '':
			return Response({'status':400, 'message': ' Ingresa un video de youtube con tu intro'})
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response({'status':201, 
			'message':'datos generales han sido creados', 
			'data': serializer.data})
		
		return Response({'status':400, 'message':'revisa tus datos'})

		

#Create list of aplicants
class ApplicantsView(APIView):
	permission_classes = [IsAuthenticated]
	
	def get(self, request):
		personas = Persona.objects.all()
		serializer = UserGeneralSerializer(personas, many=True)
		return Response(serializer.data)

# lista de roles de trabajo
class JobRolesView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		personas = Persona.objects.order_by('jobrole').distinct('jobrole')
		serializer = JobRoleListSerializer(personas, many=True)

		return Response({'status':200, 'message':'lista de roles de trabajo', 'data':serializer.data})



class PersonaViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Persona.objects.all() 
    serializer_class = UserGeneralSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
    	assigned_only=bool(self.request.query_params.get('assigned_only'))
    	queryset = self.queryset
    	if assigned_only:
           queryset = queryset.filter(persona__isnull=False)
           return queryset.filter(user=self.request.user).order_by('-first_name')
           def perform_create(self, serializer):
           	serializer.save(user=self.request.user)




	

			

