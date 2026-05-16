from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from products_api.views import api_root

urlpatterns = [
    path('', api_root),
    path('admin/', admin.site.urls),
    path('api/v1/', include('products_api.urls')),
    path('api/v1/auth/token/', TokenObtainPairView.as_view()),
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view()),
]