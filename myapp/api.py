from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapp.serializers import *

class UserList(APIView):
    def get(self,request):
        model=User.objects.all()
        serializer=User_Serializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = User_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get_user(self,Employee_id):
        try:
            model=User.objects.get(id=Employee_id)
            return model
        except User.DoesNotExist:
            return

    def get(self,request,Employee_id):
        if not self.get_user(Employee_id):
           return Response(f'User with {Employee_id} id is not found in database',status=status.HTTP_404_NOT_FOUND)
        serializer=User_Serializer(self.get_user(Employee_id))
        return Response(serializer.data)

    def put(self,request,Employee_id):
        if not self.get_user(Employee_id):
           return Response(f'User with {Employee_id} id is not found in database',status=status.HTTP_404_NOT_FOUND)
        serializer = User_Serializer(self.get_user(Employee_id),data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,Employee_id):
        if not self.get_user(Employee_id):
           return Response(f'User with {Employee_id} id is not found in database',status=status.HTTP_404_NOT_FOUND)
        model=self.get_user(Employee_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

