# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
 
class PosConfig(models.Model):
    _inherit = 'pos.config'

    value_uvt = fields.Float('Value UVT',related='company_id.value_uvt')
    qty_limit_uvt = fields.Integer('Qty limit UVT para Ticket')
    value_limit_uvt_ticket = fields.Float('Value limit ticket UVT')

    @api.onchange('qty_limit_uvt')
    def _onchange_calculate_limit_uvt_ticket(self):
        value_limit_uvt_ticket = 0
        for rec in self:
            if rec.qty_limit_uvt > 0:
                value_limit_uvt_ticket = float(rec.value_uvt) * rec.qty_limit_uvt

            rec.value_limit_uvt_ticket = value_limit_uvt_ticket

