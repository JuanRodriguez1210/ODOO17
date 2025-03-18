# -*- coding: utf-8 -*-
{
    "name": " mp info fe in ticket pos ",
    'version': '1.0',
    'author': "More Products S.A.S.",
    'website': "https://www.odoo.moreproducts.com",
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],
    'summary': 'Módulo que agrega información de facturación electrónica  en el ticket pos.',
    'description': """
- Agrega los datos del cufe, número de factura y qr de factura electrónica al ticket pos., Además de modificaciones en la estructura original del ticket.
    """,
    'data': [],
    'assets': {
        'point_of_sale._assets_pos': [
            'mp_pos_ticket_fe/static/src/js/pos_store.js',
            'mp_pos_ticket_fe/static/src/js/models.js',
            'mp_pos_ticket_fe/static/src/xml/receipt_header.xml',
            'mp_pos_ticket_fe/static/src/xml/pos_order_receipt.xml',
        ],
    },
    'application': True,
    'installable': True,
    "license": "LGPL-3",    
}
