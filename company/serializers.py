from users.models import User
from company.models import Empresa

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError

import cloudinary

from core.settings import base

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['id', 'email', 'is_active', 'is_verified']

class CompanySerializer(serializers.ModelSerializer):

	class Meta:
		model = Empresa
		fields = ['user', 'empresa', 'descrip', 'web', 'rfc', 'logo']


	def validate(self, attrs):
		rfc = attrs['rfc']
		web = attrs['web']
		items = ['https://www']
		x = [item for item in items if(item in web)]
		proof = ''
		proof = (bool(x))
		val = proof
		if val == False:
			raise serializers.ValidationError("enter valid url starting with https://www")


		if len(rfc) < 12 or len(rfc) > 13:
			raise serializers.ValidationError(" enter valid rf ")

		if rfc == 'XAXX010101000':
			raise serializers.ValidationError(" this can't be your rfc ")
		

		if any(char.islower() for char in rfc):
			raise serializers.ValidationError(" enter valid rf ")

		if not any(char.isdigit() for char in rfc):
			raise serializers.ValidationError(" enter valid rf ")



		return attrs

	"""def create(self, validated_data):
		empresa = Empresa.objects.create(**validated_data)
		image = validated_data.get('logo', None)
		if not image is None:
			upload_data = cloudinary.uploader.upload(image, folder=f'media/companies/{validated_data.get("empresa")}')
			empresa.logo = upload_data["secure_url"]
		empresa.save()
		return empresa"""

class CompanyProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Empresa
		fields = ['user', 'empresa']
		read_only_fields = ['user', 'empresa']
		
class WaitinglistSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	
	class Meta:
		model = Empresa
		fields = ['user', 'empresa', 'rfc', 'web', 'is_approved', 'is_declined', 'logo']

	def to_representation(self, instance):
		response = super().to_representation(instance)
		logo = response.pop('logo')
		response.setdefault(base.CLOUDINARY_BASE_URL+logo)
		return response

	