
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from utils.mixins import SerializerGetMethodMixin

from .models import Product
from .permissions import IsOwnerOrReady, IsSellerOrReady
from .serializers import ProductSerializerCreateOrUpdate, ProductSerializerList


class ListCreateProducts(SerializerGetMethodMixin, ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSellerOrReady]
    lookup_url_kwarg= "product_id"

    queryset = Product.objects.all()
    serializer_map = {
        "GET": ProductSerializerList,
        "POST": ProductSerializerCreateOrUpdate,
    }

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class GetIdUpdateProduct(RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReady]

    queryset = Product.objects.all()
    serializer_class = ProductSerializerCreateOrUpdate
    lookup_url_kwarg= "product_id"
