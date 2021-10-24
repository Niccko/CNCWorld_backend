import json
from django.http import JsonResponse
from django.views import View
from .dbutils import *


class CRUDObject(View):
    table_name = None
    pk_name = None
    relation = None

    def get(self, request, pk=None):
        if pk == 0:
            return JsonResponse(get_row_desc(self.table_name), safe=False)
        if pk:
            return JsonResponse(select_by_id(self.table_name, self.pk_name, pk), safe=False)
        return JsonResponse(select_all(self.table_name), safe=False)

    def post(self, request):
        data = json.loads(request.body)
        row = add_row(self.table_name, self.pk_name, data)
        return JsonResponse(row)

    def delete(self, request, pk=None):
        return JsonResponse(remove_row(self.table_name, self.pk_name, pk), safe=False)

    def put(self, request, pk=None):
        if pk:
            data = json.loads(request.body)
            return JsonResponse(update_row(self.table_name, self.pk_name, data, pk), safe=False)
