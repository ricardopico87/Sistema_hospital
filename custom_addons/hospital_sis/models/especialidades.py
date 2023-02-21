# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Especialidades(models.Model):
    _name = 'sis.especialidades'

    # definimos por donde haremos la busqueda
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', size=80, required=True, help='Aqui pones el nombre')

