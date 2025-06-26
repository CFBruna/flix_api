from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
# Essa biblioteca já tem toda a verificação de usuário, senha, token e etc. Apenas chamando a view que já está pronta você tem tudo isso.

urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
