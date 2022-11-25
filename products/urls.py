from django.urls import path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

from products.views import GetIdUpdateProduct, ListCreateProducts

urlpatterns = [
    path("products/", ListCreateProducts.as_view()),
    path("products/<str:product_id>/", GetIdUpdateProduct.as_view()),
    # path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # path("products-docs/", SpectacularSwaggerView.as_view()),
    # path("products-redoc/", SpectacularRedocView.as_view()),

]
