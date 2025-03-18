# -*- coding: utf-8 -*-
{
    'name': "Mp pos filtrar productos por campos seleccionados",

    'summary': "Limita el buscador por los campos seleccionados en la configuración del pos",

    'description': """
Limita el buscador por los campos seleccionados en la configuración del pos, el campo de Campos a filtrar productos,
Las opciones son (código de barras, referencia y nombre)
    """,

    'author': "More Products S.A.S.",
    'website': "https://www.odoo.moreproducts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale','base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/field_to_filter_pos.xml',
        'views/pos_config_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'mp_pos_limit_filter_by_barcode/static/src/**/*',
        ],
    },
}

