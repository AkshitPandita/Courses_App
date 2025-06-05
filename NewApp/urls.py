
from django.urls import path

from . import views

urlpatterns = [
    

    path('',views.New_app_view,name='new_app_view'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    
]