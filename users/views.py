from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import AuthenticationFailed

from .models import User

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


import datetime
from datetime import timedelta
import jwt
import os

from users.models import User
from users.serializers import UserSignUpSerializer, UserSerializer, ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer
from users.utils import Util
from core.settings import base

from rest_framework_simplejwt.tokens import RefreshToken



# Generates tokens manually.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Registro de usuario
class UserSignUpView(APIView):
	def post(self, request):
		serializer = UserSignUpSerializer(data= request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			user_data = serializer.data 
			user = User.objects.get(email=user_data['email'])
			token = RefreshToken.for_user(user).access_token
		
			current_site = get_current_site(request).domain
			relativeLink = base.EMAIL_VERIFY

			absurl = relativeLink+"?token="+str(token)
			# print(absurl)
			email_body = 'Hola  '+user.email+' Use este link para verificar su email: \n' + absurl 
			data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verifica tu email '}
			Util.send_email(data)

			return Response({'status': 200, 
				'payload': serializer.data, 
				'token': str(token),
				'message': 'Check your email to verify your account before login'})
		else:
			return Response({'status': 403, 'message': 'El email o password ingresados no cumplen los criterios del registro'})


# Verificacion de email
class VerifyEmailView(APIView):

	def post(self, request):
		token = request.data['token']
		if token is None:
			return Response({'status':404, 'message':'no token'})
		
		try:
			payload = jwt.decode(token, 'secret', algorithms=['HS256'])
			user = User.objects.get(id=payload['user_id'])
		
			if not user.is_verified:
				user.is_verified = True
			if not user.is_active:
				user.is_active = True
				user.save()
			return Response({'status':200, 'message': 'tu cuenta ha sido activada'})
		except jwt.ExpiredSignatureError as identifier:
			return Response({'status':400, 'error':'token expired'})
		except jwt.exceptions.DecodeError as identifier:
			return Response({'status':400, 'error':'token invalid'})
		
	
# Login de usuario
class UserLoginView(APIView):

	permissions_classes = (AllowAny,)
	
	def post(self, request):
		email = request.data['email']
		password = request.data['password']
		user = User.objects.filter(email=email).first()

		if user is None:
			return Response({'status':404, 
				'message':'User not found'})

		if not user.check_password(password):
			user.pwd_count += 1
			total_pwd = user.pwd_count
			user.save()
			print(total_pwd)
			if total_pwd >= 4:
				user.is_active = False
				user.save()
				return Response({'status': 403, 'message': 'Usuario ha sido bloqueado por demasiados intentos'})
			return Response({'status':401, 'message': 'Incorrect password'})


		

			if total_pwd >= 4:
				user.is_active = False 
				user.save()
				return Response({'status':401, 
					'message': 'Your account has been blocked'})
			return Response({'status':401,
				'message':'Incorrect Password'})

		if not user.is_verified:
			return Response({'status':401,
				'message':'Account is not verified'})

		if user.is_active == False:
			return Response({'status':403, 'message':'Your account has been block for too many attempts... Please follow the instruction to reset your password'})

		user.pwd_count = 0
		user.save()
			
		payload = {
				'id': user.id,
				'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
				'iat': datetime.datetime.utcnow()
				}

		refresh = RefreshToken.for_user(user)
		
		#token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
		
		response = Response()

		#response.set_cookie(key='jwt', value=token, httponly=True)
		#response.setdefault(key='token', value=token)

		response.data = {
				'access': str(refresh.access_token),
				'refresh': str(refresh), 
				'status': 200,
				'id': user.id,
				'role': user.role.id,
			}

		return response



# Cambiar contraseña por medio de email=========
class PasswordRecoveryEmail(APIView):
	serializer = ResetPasswordEmailRequestSerializer

	def post(self, request):
		serializer = self.serializer(data=request.data)
		email = request.data.get('email', '')

		if User.objects.filter(email=email).exists():
			user = User.objects.get(email=email)
			refresh = RefreshToken.for_user(user)
			#current_site = get_current_site(
				#request=request).domain
			relativeLink = base.FRONT_URL

			absurl = relativeLink+"?token="+str(refresh)
			email_body = 'Hola '+user.email+' Use este enlace para cambiar su contraseña   \n'+absurl
			data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Password change'}
			Util.send_email(data)

			return Response({'status':200, 'message': 'Check your email to recover your password'})
		return Response({'status':404, 'message': 'No existe un usuario con ese email'})



# Vista para escribir la nueva contraseña del usuario
class SetNewPasswordView(APIView):
	serializer = SetNewPasswordSerializer

	def patch(self, request):
		token = request.data['token']
		try:
			payload = jwt.decode(token, options={"verify_signature": False}, algorithms=['HS256'])
		except jwt.ExpiredSignatureError as identifier:
			return Response({'error':'token expired'})
		except jwt.exceptions.DecodeError as identifier:
			return Response({'error':'token invalid'})
		user = User.objects.filter(id=payload['user_id']).first()
		serializer = SetNewPasswordSerializer(data=request.data)
		if serializer.is_valid():
			password = request.data['password']
			user.set_password(password)
			user.is_active = True
			user.save()
		else: 
			return Response({'status':401, 'message': 'password must be longer than 6 charachters, contain symbols, numbers, uppercase and lowercase'})
		return Response({'status': 200, 'sucess': True, 'message': 'Password reset success'})










