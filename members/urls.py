
from django.urls import path
from members import views
from members.views import UserView, ProfileCreate, ApplicantsView, JobRolesView


urlpatterns = [
   path('profile/', views.UserView.as_view()),
   path('profile/create/', views.ProfileCreate.as_view(), name="profile"),
   path('talent/', views.ApplicantsView.as_view(), name="talent"),
   path('jobroles/', views.JobRolesView.as_view())
]