# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Consultas(models.Model):

    # Como practica ponemos el nombre comenzando con un prefijo
    _name = 'sis.consultas'

    # definimos por donde haremos la busqueda
    _rec_name='nombre'

    nombre = fields.Char(string='Nombre', size=80, required=True, help='Aqui pones el nombre')
    partner_id = fields.Many2one('res.partner', string='Paciente', ondelete='restrict')
    especialidades = fields.Many2one('sis.especialidades', string='Especialidad', ondelete='restrict')

