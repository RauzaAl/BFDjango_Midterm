from .models import Book, Journal
from rest_framework import viewsets
# from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from django.db.models import Prefetch
# from rest_framework.response import Response
from main.serializers import BookSerializer, JournalSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        print(self.request.user.role)
        if self.request.method == 'GET':
            return IsAuthenticated(),
        elif self.request.user.role == 1:
            return IsAuthenticated(),
        else:
            return IsAdminUser(),


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return IsAuthenticated(),
        elif self.request.user.role == 1:
            return IsAuthenticated(),
        else:
            return IsAdminUser(),
