from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ToDo
from .serializers import ToDoSerializer

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
