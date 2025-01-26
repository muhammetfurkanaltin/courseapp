from rest_framework import serializers
from book_api.models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    page_number = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    stock = serializers.IntegerField()
    
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.page_number = validated_data.get('page_number', instance.page_number)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.save()
        return instance