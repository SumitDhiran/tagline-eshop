from django.shortcuts import render
from .models import User,Product,Purchase
from rest_framework import viewsets,permissions,status,filters
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import UserSerializer,ProductSerializer,PurchaseSerializer
from .permissions import UserPermission,ProductPermission
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from .filter import PriceFilter

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    # permission_classes = ()

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve' or self.action == 'create':
            self.permission_classes = (permissions.AllowAny,)
        else:
            self.permission_classes = (permissions.IsAuthenticated, UserPermission,)

        return super(self.__class__, self).get_permissions()

    def get_queryset(self):
        return User.objects.all()


class PrductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['owner', 'type']
    search_fields = ['name']
    ordering_fields = ['name','created_at','updated_at']

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            self.permission_classes = (permissions.AllowAny,)
        else:
            self.permission_classes = (permissions.IsAuthenticated, ProductPermission,)

        return super(self.__class__, self).get_permissions()

    def get_queryset(self):
        return Product.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False,methods=['GET'])
    def available_products(self, request, *args, **kwargs):
        qs = Product.objects.filter(type__exact="Available")
        serializer = self.get_serializer(qs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class PurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # removing # "put", "patch", "delete",
    http_method_names = [
        "get",
        "post",
        "head",
        "options",
        "trace",
    ]

    def get_queryset(self):
        return Purchase.objects.all()

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            product_id =  request.data.get('product')
            product = Product.objects.get(id=product_id)
            if product.owner == request.user:
                return Response({"message":"Product owner and buyer cannot be same."}, status=status.HTTP_403_FORBIDDEN)
            if product.type == "Sold":
                return Response({"message":"Sold Out."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message":f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False,methods=['GET'])
    def user_purchase(self, request, *args, **kwargs):
        qs = Purchase.objects.filter(buyer=request.user)
        serializer = self.get_serializer(qs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
