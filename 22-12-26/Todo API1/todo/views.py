from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

# Create your views here.

from .models import Todo
from .serializers import TodoSerializer, TodoDetailSerializer, TodoCreateSerializer

class TodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(completed=False)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TodoCreateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
    
class TodoAPIView(APIView):
    def get(self, request , pk):
        todo = get_object_or_404(Todo, id = pk)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status = status.HTTP_200_OK)