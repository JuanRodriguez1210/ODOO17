# -*- coding: utf-8 -*-

from odoo import models, fields, api


class field_to_filter_pos(models.Model):
    _name = 'field.to.filter.pos'
    _rec_name ='name'
    name = fields.Char()
    code = fields.Char()
