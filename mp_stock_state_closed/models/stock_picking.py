# -*- coding: utf-8 -*-

from odoo import models, fields, api

#hereda módelo para agregar nuevo estado
class stock_picking(models.Model):
    _inherit = 'stock.picking'
    state = fields.Selection(selection_add=[('closed', 'Cerrado'),], ondelete={'closed': "set done"})

    #Actualiza el estado del registro
    def set_to_closed(self):
        for rec in self:
            rec.write({'state': 'closed'})





