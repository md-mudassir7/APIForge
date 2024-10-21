from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.apps import apps
from core.models import DynamicModel


class DynamicApiView(APIView):
    def get(self, request, model_name):
        try:
            model = apps.get_model("core", model_name)
            objects = model.objects.all().values()
            return Response(objects)
        except LookupError:
            return Response(
                {"error": "Model not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request, model_name):
        try:
            model = apps.get_model("core", model_name)
            obj = model.objects.create(**request.data)
            return Response({"id": obj.id}, status=status.HTTP_201_CREATED)
        except LookupError:
            return Response(
                {"error": "Model not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
