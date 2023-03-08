from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import FaqTable
from .serializers import FaqSerializer
from django.shortcuts import get_list_or_404


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


class FaqInfo(APIView):
    def get(self, request, faq_id):
        try:
            obj = FaqTable.objects.get(faq_id = faq_id)

        except FaqTable.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = FaqSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, question):
        try:
            obj = get_list_or_404(FaqTable, question=question)

        except FaqTable.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = FaqSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, faq_id):
        try:
            obj = FaqTable.objects.get(faq_id = faq_id)

        except FaqTable.DoesNotExist:
            msg = {"msg" : "not found"}

            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = FaqSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, faq_id):
        try:
            obj = FaqTable.objects.get(faq_id=faq_id)

        except FaqTable.DoesNotExist:
            msg = {"msg": "not found"}

            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = FaqSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, faq_id):
        try:
            obj = FaqTable.objects.get(faq_id = faq_id)

        except FaqTable.DoesNotExist:
            msg = {"msg" : "not found"}
            return Response(msg, status= status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"deleted"}, status=status.HTTP_204_NO_CONTENT)


