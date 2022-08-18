from rest_framework import serializers
from rest_framework.serializers import (EmailField, HyperlinkedIdentityField, ModelSerializer, SerializerMethodField, ValidationError, CharField)

from vacantes.models import Vacante
from members.models import Persona
from company.models import Empresa

class VacantesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Vacante
		fields = ['company', 'area', 'jobrole', 'tipo_trabajo', 'modalidad', 'descripcion', 'requisitos', 'video_vacante',  'pregunta_1', 'pregunta_2', 'pregunta_3', 'sueldo', 'state', 'city']


	def validate(self, attrs):
		video_vacante = attrs['video_vacante']
		q1 = attrs['pregunta_1']
		q2 = attrs['pregunta_2']
		q3 = attrs['pregunta_3']
		s = attrs['sueldo']
		
		
		if q1 is None:
			return attrs
			
		if q2 is None:
			return attrs
			
		if q3 is None:
			return attrs
			
		if s is None:
			return attrs
			
		if video_vacante is not None:
			items = ['https://www.youtube.com', '']
			x = [item for item in items if(item in video_vacante)]
			proof = ''
			proof = (bool(x))
			val = proof
			if val == False:
				raise serializers.ValidationError("Ingresa un url de youtube valido empezando con https://www")

		return attrs

class EmpresaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Empresa
		fields = ['empresa', 'is_approved']

class PersonaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Persona
		fields = ['user', 'area']

class CompanyJobListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vacante
		fields = ['id', 'company', 'area', 'jobrole', 'modalidad', 'tipo_trabajo', 'sueldo', 'descripcion', 'requisitos', 'video_vacante', 'city', 'created_at', 'is_active']

class JobsListSerializer(serializers.ModelSerializer):
	company = EmpresaSerializer(read_only=True)

	class Meta:
		model = Vacante
		fields = ['id', 'company', 'area', 'jobrole', 'modalidad', 'tipo_trabajo', 'descripcion', 'requisitos', 'sueldo', 'pregunta_1', 'pregunta_2', 'pregunta_3', 'video_vacante', 'city', 'is_active', 'created_at']
