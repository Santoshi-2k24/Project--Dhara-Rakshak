from django.urls import path
from .views import *

urlpatterns = [
    path('upload-form/', upload_area, name='upload_area'),
    path('upload/',upload_land_record_form,name='post_form'),
    path('upload-success/', upload_success, name='upload_success'),
    path('all-records/', all_land_records_view, name='get_all_land_records'),
]
