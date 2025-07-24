from django.urls import path
from .views import upload_json, all_records

urlpatterns = [
    path('upload/',upload_json, name='upload_json'),
    path('records/',all_records, name='all_records'),
]