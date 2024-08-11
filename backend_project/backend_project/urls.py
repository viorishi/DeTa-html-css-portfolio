from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView #ProjectSpecific
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView #ProjectSpecific allow to refresh tokens

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"), #ProjectSpecific
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"), #ProjectSpecific
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"), #ProjectSpecific
    path("api-auth/", include("rest_framework.urls")),#ProjectSpecific
    path("api/", include("api.urls")), # anitime we have link with api/ and do not match anyone above it will take the remain on the path and forward to api urls
]
