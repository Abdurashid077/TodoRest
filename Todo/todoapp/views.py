from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .serializer import PlanSerializer
from .models import Plan




class PlanList(ListCreateAPIView):
    serializer_class = PlanSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        plans = Plan.objects.filter(user=self.request.user)
        return plans
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GetList(RetrieveAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class UpdateList(RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class DestroyList(RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

# class CreateList(CreateAPIView):
#     queryset = Plan.objects.all()
#     serializer_class = PlanSerializer

