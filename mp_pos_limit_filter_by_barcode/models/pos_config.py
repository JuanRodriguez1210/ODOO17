# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pos_config(models.Model):
     _inherit = 'pos.config'

     field_to_filter = fields.Many2many('field.to.filter.pos', string='Campos a filtrar')




