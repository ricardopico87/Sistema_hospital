# -*- coding: utf-8 -*-
from odoo import api, fields, models


class res_partner(models.Model):

    # Como practica ponemos el nombre comenzando con un prefijo
    _inherit = 'res.partner'

    rut = fields.Char(string='Rut', size=10, help='Este es rut')
    edad = fields.Integer(string='Edad', size=3, help='Aqui pones la edad')
    profesion = fields.Char(string='Profesion', size=10, help='Este es rut')

