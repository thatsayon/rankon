from django.urls import path
from . import views

urlpatterns = [
    path('rankers/', views.RankerView.as_view(), name="rankers"),
    path('vote/<int:pk>/', views.RankerVoteAPIView.as_view(), name="vote"),
]
