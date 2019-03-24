import urllib.request

from celery import shared_task
from django.db import transaction
import json

from app_linkup.models.categoria import Categoria


@shared_task(bind=True)
@transaction.atomic()
def task_guardar_categorias(self):
    link = "http://ec2-18-208-107-13.compute-1.amazonaws.com:9000/categories/"
    response = urllib.request.urlopen(link)
    encoding = response.info().get_content_charset('utf8')
    categoria_list = json.loads(response.read().decode(encoding))

    for categoria_data in categoria_list:
        categoria_bd = Categoria.objects.filter(nombre=categoria_data['name'])

        if len(categoria_bd) == 0:
            categoria = Categoria(nombre=categoria_data['name'], descripcion=categoria_data['description'],
                                  imagen=categoria_data['image'], orden=categoria_data['order'],
                                  estado=categoria_data['status'])
            categoria.save()
