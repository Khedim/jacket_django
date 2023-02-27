from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import api_view
from django.db.models import Q

# Create your views here.
class ProductsListAPI(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get(self, request, category_slug, product_slug, format=None):
        product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetailAPI(APIView):
    def get(self, request, category_slug, format=None):
        category = get_object_or_404(Category, slug=category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
@api_view(['GET'])
def search(request):
    query = request.GET.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"Products": []})