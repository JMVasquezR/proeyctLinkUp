from django.db import models
import re


def get_value_from_model_choice(tuple_of_choices, key):
    '''
    Este metodo se encargara de obtener el valor de la clave de un choice para djnago models
    :param tuple_of_choices:
    :param key:
    :return:
    '''
    for item in tuple_of_choices:
        if item[1] == key:
            return item[0]
    raise Exception('Clave no encontrada')


def clean_text(text):
    if text:
        text = text.strip()
        text = re.sub(r'\s+', ' ', text)
        text = text.lower()
        return text
    else:
        return ''


class CleanCharField(models.CharField):
    def get_prep_value(self, value):
        return clean_text(super(CleanCharField, self
                                ).get_prep_value(value))

    def pre_save(self, model_instance, add):
        return clean_text(super(CleanCharField, self
                                ).pre_save(model_instance, add))
