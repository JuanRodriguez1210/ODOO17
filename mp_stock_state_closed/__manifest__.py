# -*- coding: utf-8 -*-
{
    'name': "mp Etapa cerrado en inventario",

    'summary': "Agrega la etapa de cerrado en las operaciones de inventario.",

    'description': """
Permite pasar de etapa terminado a cerrado las operaciones del inventario, mediante el botón cerrar, este botón solo es visible cuando 
la operación se encuentre en estado terminado.
    """,

    'author': "More Products S.A.S.",
    'website': "https://www.odoo.moreproducts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        'views/stock_picking_form_view.xml',

    ],
}

