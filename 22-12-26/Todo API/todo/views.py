from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

from .models import Todo
from .serializers import TodoSerializer

class TodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(complted=False)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)