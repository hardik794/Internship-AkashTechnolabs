from django.urls import path
from . import views
urlpatterns = [
    path('', views.studentlist.as_view(),name='data'),
]