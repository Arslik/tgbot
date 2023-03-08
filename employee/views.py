from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from .models import Employees
from .serializer import EmployeeSerializer


class EmployeeDetail(APIView):
    def get(self, request):
        obj = Employees.objects.all()
        serializer = EmployeeSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class EmployeeInfo(APIView):
    def get(self, request, employee_id):
        try:
            obj = Employees.objects.get(employee_id=employee_id)

        except Employees.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, employee_id):
        try:
            obj = Employees.objects.get(employee_id=employee_id)

        except Employees.DoesNotExist:
            msg = {"msg": "not found"}

            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, employee_id):
        try:
            obj = Employees.objects.get(employee_id=employee_id)

        except Employees.DoesNotExist:
            msg = {"msg": "not found"}

            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, employee_id):
        try:
            obj = Employees.objects.get(employee_id=employee_id)

        except Employees.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response({"msg": "deleted"}, status=status.HTTP_204_NO_CONTENT)


class EmployeeUsernameSearch(generics.ListAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return Employees.objects.filter(username__icontains=username)


class EmployeeEmailSearch(generics.RetrieveAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employees.objects.all()

    def get_object(self):
        email = self.request.data['email']
        try:
            return Employees.objects.get(email=email)
        except Employees.DoesNotExist:
            return None


class EmployeePhoneSearch(generics.RetrieveAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employees.objects.all()

    def get_object(self):
        phone_number = self.request.data['phone_number']
        try:
            return Employees.objects.get(phone_number=phone_number)
        except Employees.DoesNotExist:
            return None
