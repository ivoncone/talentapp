from django.urls import path
from company import views
from company.views import CompanyProfileView ,CompanyView, CompanyWaitingListView, RetrieveCompanyView

urlpatterns = [
	path('company/', views.CompanyProfileView.as_view()),
	path('company/create/', views.CompanyView.as_view(), name='company'),
	path('waitingList/', views.CompanyWaitingListView.as_view(), name='waiting-list'),
	path('waitingList/<company_id>', views.RetrieveCompanyView.as_view()),
]