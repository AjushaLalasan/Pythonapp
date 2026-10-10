from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services_list, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('projects/', views.projects_list, name='projects'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('about/', views.about_us, name='about'),
    path('contact/', views.contact, name='contact'),
    # AJAX API routes
    path('api/quote/', views.api_request_quote, name='api_request_quote'),
    path('api/projects/<int:pk>/', views.api_project_detail, name='api_project_detail'),
]
