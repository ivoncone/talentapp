from users.models import User
from members.models import Persona, DatosAcademicos
from intereses.models import Area, jobRole

from rest_framework import serializers
from rest_framework.serializers import (EmailField, PrimaryKeyRelatedField, HyperlinkedIdentityField, ModelSerializer, SerializerMethodField, ValidationError, CharField)


class datosAcademicosSerializer(serializers.ModelSerializer):
	class Meta:
		model = DatosAcademicos
		fields = ['nivel_academico', 'nombre', 'institucion', 'duracion', 'status']

class AreaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Area
		fields = '__all__'

class jobRoleSerializer(serializers.ModelSerializer):
	class Meta:
		model = jobRole
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'email', 'is_active', 'is_verified', 'created_at']

		extra_kwargs = {
		'password':{'write_only': True},
		}
# Get detail data from logged users
class UserProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = Persona
		fields = ['user', 'first_name', 'last_name', 'state', 'jobrole', 'image', 'video']
		read_only_fields = ['user', 'first_name', 'last_name', 'state', 'area', 'video']


class UserGeneralSerializer(serializers.ModelSerializer):
	datosAcademicos = datosAcademicosSerializer(many=True)
	
	
	class Meta:
		model = Persona
		fields = ['user',
			'first_name', 
			'last_name', 
			'last_name_m', 
			'genero', 
			'birth_date', 
			'civil_status', 
			'age',
			'state', 
			'residence',
			'datosAcademicos',
			'area', 
			'jobrole', 
			'modalidad', 
			'tipo_trabajo', 
			'video']


	def validate(self, attrs):
		video = attrs['video']
		if video is None:
			return video
		if video is not None:
			items = ['https://www.youtube.com']
			x = [item for item in items if(item in video)]
			proof = ''
			proof = (bool(x))
			val = proof
			if val == False:
				raise serializers.ValidationError("debe ser un video de youtube")

		return attrs

	def create(self, validated_data):
		datosAcademicos = validated_data.pop('datosAcademicos')
		persona = Persona.objects.create(**validated_data)
		for dato in datosAcademicos:
			a = DatosAcademicos.objects.create(nombre=dato["nombre"], 
				nivel_academico=dato['nivel_academico'], 
				institucion=dato['institucion'],
				duracion=dato['duracion'], 
				status=dato['status'])
			persona.datosAcademicos.add(a)
		return persona


class JobRoleListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Persona
		fields = ['jobrole']
		


	


	

			



	