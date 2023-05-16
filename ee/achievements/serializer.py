from rest_framework import serializers
from .models import Books

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

    def create(self,validated_data):
        Book = Books.objects.create(name=validated_data.get('name'),
                                           year=validated_data.get('year'),
                                           author=validated_data.get('author'))
        return Book
