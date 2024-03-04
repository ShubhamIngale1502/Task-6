from django.urls import path
from .views  import Uploadfile,Details

urlpatterns = [
    path('add/',Uploadfile.as_view()),
    path('add/<int:pk>/',Details.as_view())
]
