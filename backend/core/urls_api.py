from django.urls import path, include

urlpatterns = [
    path('assets/', include('assets.urls_api')),
]