from django.urls import path
from vacantes import views

from vacantes.views import SearchView, DetailVacanteView, CreateVacanteView, CompanyJobsListView, CompanyAreaJobsListView, CompanyTipoJobsListView, CompanyModJobsListView


urlpatterns = [
	path('vacantes/create', views.CreateVacanteView.as_view(), name='vacante'),
	path('vacantes/', views.SearchView.as_view(), name='vacantes-list'),
	path('vacantes/<int:vacante_id>', views.DetailVacanteView.as_view()),
	path('vacantes/company/', views.CompanyJobsListView.as_view()),
	path('vacantes/company/area/<int:area_id>', views.CompanyAreaJobsListView.as_view()),
	path('vacantes/company/tipo/<int:tipo_trabajo_id>', views.CompanyTipoJobsListView.as_view()),
	path('vacantes/company/mod/<int:modalidad_id>', views.CompanyModJobsListView.as_view()),
]