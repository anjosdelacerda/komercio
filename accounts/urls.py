from django.urls import path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

from .views import (AccountChangeActiveView, AccountFilterView,
                    AccountUpdateView, AccountView, LoginView)

urlpatterns = [
    path("accounts/", AccountView.as_view()),
    path("accounts/<str:account_id>/", AccountUpdateView.as_view(), name="update_user"),
    path("accounts/<str:account_id>/management/", AccountChangeActiveView.as_view() ),
    path("login/", LoginView.as_view(),  name="loggedin"),
    path("accounts/newest/<int:num>/", AccountFilterView.as_view()),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view()),
    path("redoc/", SpectacularRedocView.as_view()),




]
