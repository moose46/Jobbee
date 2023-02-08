from django.urls import path

from . import views

urlpatterns = [
    path("jobs/", views.getAllJobs, name="jobs"),
    path("jobs/new/", views.newJob, name="new_job"),
    path("job/<str:pk>/", views.getJob, name="job"),
    path("job/<str:pk>/update/", views.updateJob, name="update_job"),
]
