from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.aid_home, name='aid_home'),
    path('apply/', views.apply_for_aid, name='apply_for_aid'),
    path('apply/confirmation/', views.aid_confirmation, name='aid_confirmation'),
    path('admin/manage/', views.manage_aid_applications, name='manage_aid_applications'),
    path('admin/distribute/<int:beneficiary_id>/', views.distribute_aid, name='distribute_aid'),
    path('admin/distribute/confirmation/', views.distribution_confirmation, name='distribution_confirmation'),
    path('admin/distribute/', views.select_beneficiary, name='select_beneficiary'),
    path('delete/<int:distribution_id>/', views.delete_distribution, name='delete_distribution'),
    path('admin/beneficiary/delete/<int:beneficiary_id>/', views.delete_beneficiary, name='delete_beneficiary'),
]