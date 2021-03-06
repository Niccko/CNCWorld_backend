import dataclasses
from enum import Enum

from django.apps import apps
from django.core.exceptions import *
from .models import *
from .serializers import *
from django.db import connection


def _dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def _process_input(data):
    for k in data:
        if isinstance(data[k], str):
            data[k] = f"'{data[k]}'"


def get_table_list():
    app_models = [x for x in list(apps.get_app_config('api').get_models()) if not x.Extra.service]
    return list(map(lambda m: {"table_name": m._meta.model_name}, app_models))


def get_row_desc(table_name):
    ser = name_to_serializer.get(table_name)
    if not ser:
        return None
    model = ser.Meta.model
    field_list = model._meta.get_fields()
    result = []
    for field in field_list:
        if not isinstance(field, ManyToOneRel) \
                and not isinstance(field, ManyToManyRel) \
                and (model.Extra.custom_id | (field.name != "id")):
            rel = field.related_model.__name__.lower() if field.related_model else ""
            many = isinstance(field, ManyToManyField)
            result.append({"column_name": field.name, "related_to": rel, "many": many})
    return result


def apply_filter(objects, filter):
    pass


def resolve_object(model, data, obj=None):
    if not obj:
        if model.objects.filter(pk=data.get("id")):
            raise BadRequest(f"Object of type {model.__name__} with id={data['id']} already exists")
        obj = model()
    for key in data:
        field = model._meta.get_field(key)
        if isinstance(field, ForeignKey) or isinstance(field, ManyToManyField):
            remote_model = field.related_model
            if isinstance(data[key], list):
                objects = []
                for i in data[key]:
                    objects.append(remote_model.objects.get(pk=i))
                data[key] = objects
            else:
                data[key] = remote_model.objects.get(pk=data[key])
            if isinstance(field, ManyToManyField):
                obj.save()
                getattr(obj, key).set(data[key])
                continue
        setattr(obj, key, data[key])
    return obj
