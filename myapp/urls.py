from django.urls import path
from .views import (home, job_list, job_detail, create_job, update_job, delete_job, applications, admin_panel, update_status,
    create_category, update_category, delete_category, create_company, update_company, delete_company,
    create_application, update_application, delete_application)

urlpatterns = [
    path('', home, name='home'),
    path('jobs/', job_list, name='job_list'),
    path('jobs/<int:pk>/', job_detail, name='job_detail'),
    path('create_job/', create_job, name='create_job'),
    path('update_job/<int:pk>/', update_job, name='update_job'),
    path('delete_job/<int:pk>/', delete_job, name='delete_job'),
    path('applications/', applications, name='applications'),
    path('admin_panel/', admin_panel, name='admin_panel'),
    path('update_status/<int:pk>/', update_status, name='update_status'),
    path('create_category/', create_category, name='create_category'),
    path('update_category/<int:pk>/', update_category, name='update_category'),
    path('delete_category/<int:pk>/', delete_category, name='delete_category'),
    path('create_company/', create_company, name='create_company'),
    path('update_company/<int:pk>/', update_company, name='update_company'),
    path('delete_company/<int:pk>/', delete_company, name='delete_company'),
    path('create_application/', create_application, name='create_application'),
    path('update_application/<int:pk>/', update_application, name='update_application'),
    path('delete_application/<int:pk>/', delete_application, name='delete_application'),
]
