from odoo import fields,models,api


class ResPartner(models.Model):
   _inherit = 'res.partner.bank'

   account_type = fields.Selection([('ahorros', 'AHORROS'),('corriente', 'CORRIENTE')],'Tipo de Cuenta',tracking=True, ondelete="RESTRICT")
