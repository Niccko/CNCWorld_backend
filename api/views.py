import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from .dbutils import *
from rest_framework.views import APIView
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
        limit = f"LIMIT {data['limit']}" if data and data.get('limit') else ''
        order = f"ORDER BY {','.join(data['order_by'])}" if data and data.get('order_by') else ''
        where = f"WHERE {data['filter']}" if data and data.get('filter') else ''
        field_list = [model._meta.pk.name] + data['fields'] if data and data.get('fields') else [f.name for f in model._meta.fields]
        data_query = f"SELECT * FROM {table_name} {where} {order} {limit}"
        objects = serializer(model.objects.raw(data_query), many=True).data
        print(data.get('fields'))
        for ent in objects:
            for key in list(ent.keys()):
                if key not in field_list:
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
        pk = json.loads(request.body).get('pk')
        obj = resolve_object(model, data, model.objects.get(**pk))
        obj.save()
        return JsonResponse(serializer(model.objects.get(**pk)).data, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class DeleteView(APIView):
    def delete(self, request, table_name):
        serializer = name_to_serializer.get(table_name)
        model = serializer.Meta.model
        pk = json.loads(request.body).get('pk')
        obj = model.objects.filter(**pk).first()
        obj_ser = serializer(obj).data
        obj.delete()
        return JsonResponse(obj_ser, safe=False)
