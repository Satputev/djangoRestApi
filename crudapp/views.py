from django.shortcuts import render
# Create your views here.
from rest_framework import status

from  crudapp.models import EmployeeModel
from rest_framework.views import APIView
from rest_framework.response import Response
from crudapp.serializers import EmployeeSerializer
class Employee(APIView):
    def get(self,request):
        emp=EmployeeModel.objects.all()
        serializer=EmployeeSerializer(emp,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get_object(self,id):
        try:
            emp = EmployeeModel.objects.get(eid=id)
        except EmployeeModel.DoesNotExist:
            emp=None
        return emp

    def put(self,request,pk,format=None):
        emp=self.get_object(pk)

        serializer=EmployeeSerializer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,fromat=None):


            emp=self.get_object(pk)
            if emp:
                serilizer=EmployeeSerializer(emp)
                emp.delete()
                return Response(serilizer.data,status=status.HTTP_200_OK)
            return Response( status=status.HTTP_500_INTERNAL_SERVER_ERROR)




