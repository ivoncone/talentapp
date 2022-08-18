from django.shortcuts import render, get_object_or_404


# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from users.models import User
from company.models import Empresa
from company.serializers import UserSerializer, CompanyProfileSerializer, CompanySerializer, WaitinglistSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

from company.engines import Util

# Create company view
class CompanyView(APIView):
	permission_classes = [IsAuthenticated, ]
	parser_classes = (JSONParser, MultiPartParser, FormParser)

	def post(self, request):
		
		data = request.data 
		serializer = CompanySerializer(data=data)
		user = request.data.get('user', '')
		empresa = request.data.get('empresa', '')
		descrip = request.data.get('descrip', '')
		web = request.data.get('web', '')
		rfc = request.data.get('rfc', '')
		if Empresa.objects.filter(user=user).exists():
			return Response({'status':400, 'message': 'Este usuario ya tiene una empresa'})
		if empresa == '':
			return Response({'status':400, 'message': 'ingresa el nombre de tu empresa'})
		if descrip == '':
			return Response({'status':400, 'message': 'ingresa una descripcion de las actividades que realiza tu negocio'})
		if web == '':
			return Response({'status':400, 'message': 'debes ingresar un sitio web'})
		if rfc == '':
			return Response({'status':400, 'message': 'debes ingresar el rfc de tu negocio'})
		if Empresa.objects.filter(web=web).exists():
			return Response({'status':400, 'message': 'empresa con este sitio web ya existe'})
		if Empresa.objects.filter(rfc=rfc).exists():
			return Response({'status':400, 'message': 'empresa con este rfc ya existe'})
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response({'status': 201, 
				'message': 'Espera a que tu empresa sea verificada por medio de tu rfc',
				'data': serializer.data})
		return Response({'status': 400, 'message': 'ingresa un rfc valido'})

#una sola empresa
class CompanyProfileView(APIView):
	parser_classes = [IsAuthenticated]
	parser_classes = (JSONParser, MultiPartParser, FormParser)

	def get(self, request):
		user = User.objects.get(email=request.user)
		if Empresa.objects.filter(user=user).exists():
			company = Empresa.objects.filter(user=user).first()
			serializer = CompanyProfileSerializer(company)
			return Response({'status':200, 'data': serializer.data})
		return Response({'status':404, 'message': 'este solicitante no ha sido creado'})



# All companies in waiting list to be verified
class CompanyWaitingListView(APIView):
	permission_classes = [IsAuthenticated, ]
	parser_classes = (JSONParser, MultiPartParser, FormParser)

	def get(self, request):
		companies = Empresa.objects.filter(is_approved=False, is_declined=False)
		serializer = WaitinglistSerializer(companies, many=True)
		return Response({'status': 200,
				'message': 'usuario en espera de ser verificados',
				'data': serializer.data})

# Manually verification for each company profile
class RetrieveCompanyView(APIView):
	permission_classes = [IsAuthenticated, ]

	def get(self, request, company_id):
		company_obj = get_object_or_404(Empresa, pk=company_id)
		serializer = WaitinglistSerializer(company_obj)
		return Response({'status': 200, 'data': serializer.data})

	def put(self, request, company_id):
		company_obj = get_object_or_404(Empresa, pk=company_id)
		serializer = WaitinglistSerializer(instance=company_obj, data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		if company_obj.is_approved == True:
			email = company_obj.user.email
			email_body = 'Bienvenido '+company_obj.empresa+' a Get Talent app, tu empresa ha sido verificada ahora puedes publicar vacantas\n'
			data = {'email_body': email_body, 'to_email': email, 'email_subject': 'Confirmación de verificacion de empresa'}
			Util.send_email(data)
			return Response({'status': 200, 'message': 'company verification success', 'data': serializer.data})
		if company_obj.is_declined == True:
			email = company_obj.user.email
			email_body = 'Lo sentimos '+company_obj.empresa+' por parte del equipo de Get Talent app, te informamos que no podemos crear el perfil de tu empresa.\n'
			data = {'email_body': email_body, 'to_email': email, 'email_subject': 'Confirmación de verificacion de empresa'}
			Util.send_email(data)
			return Response({'status': 200, 'message': 'company application declined'})

		


