from django.urls import path
from base.views import job_list

urlpatterns = [
    path('jobs/', job_list, name='job-list'),
]