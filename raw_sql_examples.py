from django.db import connection
from collections import namedtuple

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def select(sql, *, return_type=dictfetchall):
    with connection.cursor() as cur:
        cur.execute(sql)
        return return_type(cur)

def call_proc(proc_name, *args, return_type=dictfetchall):
    with connection.cursor() as cur:
        cur.callproc(proc_name, args)
        return return_type(cur)


call_proc('test', 1, 'name', return_type=namedtuplefetchall)
result = select('SELECT nome from test', return_type=namedtuplefetchall)
result.nome

# Retornando Models
Person.objects.raw('SELECT * FROM myapp_person'):
Person.objects.raw('SELECT id, first_name, last_name, birth_date FROM myapp_person')
Person.objects.raw('SELECT last_name, birth_date, first_name, id FROM myapp_person')
Person.objects.raw('SELECT first AS first_name, last AS last_name, bd AS birth_date, pk AS id, FROM some_other_table')

name_map = {'first': 'first_name', 'last': 'last_name', 'bd': 'birth_date', 'pk': 'id'}
Person.objects.raw('SELECT * FROM some_other_table', translations=name_map)