from applications.models import Application
from members.models import Persona
from vacantes.models import Vacante
from vacantes.models import Empresa

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Empresa
		fields = ['empresa']

class PersonaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Persona
		fields = ['first_name', 'last_name', 'video']
		
class VacantesSerializer(serializers.ModelSerializer):
	company = CompanySerializer(read_only=True)

	class Meta:
		model = Vacante
		fields = ['id', 'company', 'area', 'jobrole', 'modalidad', 'tipo_trabajo', 'sueldo', 'is_active']



class ApplicationSerializer(serializers.ModelSerializer):
	vacante = VacantesSerializer(read_only=True)

	class Meta:
		model = Application
		fields = ['id', 'vacante', 'persona', 'video', 'is_active']



class ApplicationCompanySerializer(serializers.ModelSerializer):
	persona = PersonaSerializer(read_only=True)
	vacante = VacantesSerializer(read_only=True)

	class Meta:
		model = Application
		fields = ['id', 'vacante', 'persona', 'video', 'is_active']


class ApplicationCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Application
		fields = ['id', 'vacante', 'persona', 'video']