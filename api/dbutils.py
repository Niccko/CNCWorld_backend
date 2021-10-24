import dataclasses
from enum import Enum
from .models import *
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
    with connection.cursor() as cur:
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ")
        return _dictfetchall(cur)


def get_row_desc(table_name):
    with connection.cursor() as cur:
        cur.execute(f"SELECT column_name, data_type, is_nullable "
                    f"FROM information_schema.columns WHERE table_name = '{table_name}'")
        return _dictfetchall(cur)


def resolve_object(model, data, obj=None):
    if not obj:
        obj = model.objects.create()
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
                getattr(obj, key).set(data[key])
                continue
        setattr(obj, key, data[key])

    return obj
