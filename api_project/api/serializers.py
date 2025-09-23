from rest_framework import serializers
from .models import Book   # import the Book model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book          # tell DRF which model to serialize
        fields = '__all__'    # include all fields (title, author, etc.)
