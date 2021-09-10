from django.urls import include, path
from . import views
from .apiviews import PollListAPIView, PollDetailAPIView

urlpatterns = [
    # Use Django to build API start
    path('', views.polls_list, name='polls'),
    path('<int:pk>', views.polls_detail, name='detail'),
    # Use Django to build API end

    # Use APIView to build API start
    path('apiview/', PollListAPIView.as_view(), name='poll_list'),
    path('apiview/<int:pk>', PollDetailAPIView.as_view(), name='detail'),
    # Use APIView to build API end
]
