from rest_framework import serializers
from .models import FaqTable


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqTable
        fields = ["faq_id", "question", "answer"]
