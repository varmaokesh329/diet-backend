from django.urls import path
from .views import ai_diet

urlpatterns = [
    path('ai-diet/', ai_diet),
]