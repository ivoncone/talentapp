from django.urls import path
from applications import views

from applications.views import ApplicationListView, ApplicationCreateView, ApplicationCompanyView

urlpatterns = [
	path('applications/', views.ApplicationListView.as_view()),
	path('applications/create/', views.ApplicationCreateView.as_view()),
	path('applications/company/', views.ApplicationCompanyView.as_view()),
]

