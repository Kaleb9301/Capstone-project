from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
from django.contrib.auth.models import User

from .serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def sayHello(request):
    return HttpResponse('Hello World')


def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    


class bookingview(APIView):
    def get(self, request):
        items  = Booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data) # Return JSON
    
    
class MenuItemView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer 

class SingleMenuItem(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})