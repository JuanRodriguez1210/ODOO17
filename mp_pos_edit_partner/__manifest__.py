# -*- coding: utf-8 -*-
{
    'name': "mp edición campos partner pos ",

    'summary': "Traduce los campos del partner en el formulario del pos, y agrega como requeridos campos adicionales",

    'description': """
Traduce los campos del partner en el formulario del pos (ciudad,calle,telefono, celular, Código de barras), y agrega como requeridos (celular y número de documento)
    """,

    'author': "More Products S.A.S.",
    'website': "https://www.odoo.moreproducts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '17.0',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'mp_pos_edit_partner/static/src/**/*'
        ],
    },
}

