from rest_framework import serializers
from product.models import Product ,Category ,ProductDetail


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = '__all__'
        
        
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail 
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer(many = True)
    # detail = ProductDetailSerializer(many = False)
    class Meta:
        model = Product 
        fields = '__all__'
        
        