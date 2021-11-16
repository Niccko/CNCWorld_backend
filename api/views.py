import json

from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view

from .dbutils import *
from rest_framework.views import APIView
from django.db.models import F
from django.db import connection
from .serializers import *


def process_input(data):
    for k in data:
        if isinstance(data[k], str):
            data[k] = f"'{data[k]}'"


@api_view(http_method_names=['GET'])
def get_table_list_view(request):
    return JsonResponse(get_table_list(), safe=False)


@api_view(http_method_names=['GET'])
def get_table_desc(request, table_name):
    return JsonResponse(get_row_desc(table_name), safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class SelectView(APIView):
    def post(self, request, table_name):
        serializer = name_to_serializer[table_name]
        model = serializer.Meta.model
        data = json.loads(request.body) if request.body else None
        fields = data.get("fields")
        objects = serializer(model.objects.all(), many=True).data
        if fields and len(fields) > 0:
            for ent in objects:
                for key in list(ent.keys()):
                    if key not in fields:
                        del ent[key]
        return JsonResponse(objects, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class InsertView(APIView):
    def post(self, request, table_name):
        serializer = name_to_serializer.get(table_name)
        model = serializer.Meta.model
        data = json.loads(request.body).get('data')
        obj = resolve_object(model, data)
        obj.save()

        return JsonResponse(serializer(obj).data, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UpdateView(APIView):
    def patch(self, request, table_name):
        serializer = name_to_serializer.get(table_name)
        model = serializer.Meta.model
        data = json.loads(request.body).get('data')
        pk = json.loads(request.body).get('id')
        query_set = model.objects.filter(id=pk)
        if not query_set:
            return HttpResponse(f"Object of type '{table_name}' with id = '{pk}' does not exits.",
                                status=status.HTTP_404_NOT_FOUND)
        obj = resolve_object(model, data, query_set.first())
        obj.save()
        return JsonResponse(serializer(model.objects.get(id=pk)).data, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class DeleteView(APIView):
    def delete(self, request, table_name):
        serializer = name_to_serializer.get(table_name)
        model = serializer.Meta.model
        pk = json.loads(request.body).get('id')
        obj = model.objects.filter(id=pk)
        if not obj:
            return HttpResponse(f"Object of type '{table_name}' with id = '{pk}' does not exits.",
                                status=status.HTTP_404_NOT_FOUND)
        obj_ser = serializer(obj.first()).data
        obj.first().delete()
        return JsonResponse(obj_ser, safe=False)
