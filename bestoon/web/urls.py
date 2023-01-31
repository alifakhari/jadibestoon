from django.urls import include, path
from . import views

urlpatterns = [
    path('submit/expense/', views.submit_expense, name='submit_expense'),
    path('', views.blank_response, name='submit_expense'),
]