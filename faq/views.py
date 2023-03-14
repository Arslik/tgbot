from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from .models import FaqTable
from .serializers import FaqSerializer
from django.shortcuts import get_list_or_404
from django.contrib.auth.models import User


class FaqDetails(APIView):
    def get(self, request):
        obj = FaqTable.objects.all()
        serializer = FaqSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FaqSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class FAQByQueryAPIView(generics.RetrieveAPIView):
    serializer_class = FaqSerializer
    queryset = FaqTable.objects.all()

    def get_object(self):
        query_type = self.request.GET.get('type', None)
        query_value = self.request.GET.get('value', None)
        if not query_type or not query_value:
            return None
        try:
            if query_type == 'id':
                return FaqTable.objects.get(faq_id=query_value)
        except FaqTable.DoesNotExist:
            pass
        return None

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



