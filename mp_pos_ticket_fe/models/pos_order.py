# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PosOrder(models.Model):
    _inherit = 'pos.order' 
    
    def get_invoice_info(self,order_id):
        invoice = self.env['account.move'].search([('id','=',order_id)])
        info_factura = {}
        if invoice:
            info_factura =  {
                'invoice_number': invoice.name,
                'invoice_date': invoice.invoice_date,
                'customer_name': invoice.partner_id.name,
                'total_amount': invoice.amount_total,
                'amount_due': invoice.amount_residual,
                
            }
            #Valida la información del documento dian
            if invoice.dian_document_lines:
                #filtra documento dian
                info_factura['cufe'] = invoice.dian_document_lines[0].cufe_cude
                info_factura['resolución'] = invoice.journal_id.resolution_text           
                info_factura['qr'] = invoice.dian_document_lines[0].qr_image          
           

        return info_factura

