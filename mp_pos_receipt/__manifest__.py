# -*- coding: utf-8 -*-
{
    'name': "Mp  Ajustes tirilla pos",

    'summary': "Agregar datos del cliente a la tirilla  pos",

    'description': """
Agregar datos del cliente como  nombre y nit a la tirilla  pos
    """,

    'author': "More Products S.A.S.",
    'website': "https://www.odoo.moreproducts.com",

    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'mp_pos_receipt/static/src/**/*',
        ],
    },
}

