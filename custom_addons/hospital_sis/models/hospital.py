# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Hospital(models.Model):
    _name = 'sis.hospital'

    # definimos por donde haremos la busqueda
    _rec_name = 'nombre'

    nombre = fields.Char('Nombre', size=80, required=True, help='Aqui pones el nombre')
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    is_pedriatico = fields.Boolean(string='Is Pedriatico', help='Este hospital es pedriatico?')
