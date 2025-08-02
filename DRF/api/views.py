from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.response import Response
from .serializers import ProductSerializer
from product.models import Product
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from product.views import IsServiceProvider,IsClient
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRoutes(request):
    
    routes = [
        {'GET':'/api/products'},
        {'GET':'/api/products/id'},
        
        
        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},

    ]
    
    return Response(routes)


@api_view(['GET'])
def getProducts(request):
    
    Products = Product.objects.all()
    serializer = ProductSerializer(Products,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request,pk):
    
    Products = Product.objects.get(id=pk)
    serializer = ProductSerializer(Products,many = False)
    return Response(serializer.data)

# CBV
class ProductList(APIView):
    def get(self,request):
        product = Product.objects.all()
        serializer = ProductSerializer(product , many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ProductDetail(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# CBV
#generic view

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


#generic view


#ViewSet

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsClient]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name', 'price']
    search_fields = ['name']
#ViewSet

