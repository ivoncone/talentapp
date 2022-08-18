
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User
from members.serializers import UserGeneralSerializer
Persona_URL = reverse('persona:members-list')

class PrivateMemberApiTest(TestCase): #Test the private member api
 
 def setUp(self):
  self.client = APIClient()
  self.user = get_user_model().objects.create_user(
   'ksarthak4ever@gmail',
   'hakunam@tata2022',
   1
  )
  self.client.force_authenticate(self.user)

def test_retrieve_ingredients_list(self): #Test retrieving a list of members
  Persona.objects.create(user=self.user,  first_name='Carolina',  last_name ='Mendoza', 
  last_name_m='Correa', genero=1,
  birth_date='1989-04-23', civil_status=1, age=33,
  state=3, datosAcademicos(niivel_academico=1, nombre='tecnologia de la informacion', institucion='buap', duracion='2011-2014', status=1)
  residence='utopia', area=1, jobrole=1, modalidad=1, tipo_trabajo=1)

res = self.client.get(Persona_URL)
persona = Persona.objects.all().order_by('-first_name')
  serializer = UserGeneralSerializer(personas, many=True)
  self.assertEqual(res.status_code, status.HTTP_200_OK)
  self.assertEqual(res.data, serializer.data)

def test_create_persona_successful(self): #Testing create a new ingredient
  payload = {'first_name':'Carolina',  'last_name':'Mendoza', 
          'last_name_m':'Correa', 'genero':1,
          'birth_date':'1989-04-23', 'civil_status':1, 'age':33,
          'state':3, datosAcademicos(niivel_academico=1, nombre='tecnologia de la informacion', institucion='buap', duracion='2011-2014', status=1)
          'residence':'utopia', 'area':1, 'jobrole':1, 'modalidad':1, 'tipo_trabajo':1}
  self.client.post(INGREDIENTS_URL, payload)
  exists =  Persona.objects.filter(
    user = self.user,
    first_name = payload['first_name'],).exists() #chechking if ingredient exists. exists() function will return boolean true or false value
  self.assertTrue(exists)