from django.shortcuts import render
from .serializer import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



class Home(APIView):
    def get(self, request, *args, **kwargs):
        sample=Student.objects.all()
        serializer=StudentSerializer(sample, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    def delete(self,request):
        sample=Student.objects.get(id=request.data['id'])
        context={
            'id':sample.id,
            'message': "data deleted"
        }
        print(1)
        sample.delete()
        return Response(context,status=status.HTTP_200_OK)
    def patch(self,request):
        sample=Student.objects.get(id=request.data['id'])
        serializer=StudentSerializer(data=request.data, instance=sample)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
         
    
