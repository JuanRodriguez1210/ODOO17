# -*- coding: utf-8 -*-
{
    'name': "Mp Anticipo de Proveedores",
    'summary': "Mp Anticipo de Proveedores",
    'description': """
            Mp Anticipo de Proveedores
    """,
    'author': "More Products S.A.S.",
    'website': "https://www.odoo.moreproducts.com",
    'category': 'Account',
    'version': '0.1',
    'depends': [
        'base',
        'account',
        'hr_expense',
        'purchase',
        'product',
        ],
    'data': [
        'security/security_group.xml',
        'security/ir.model.access.csv',
        'data/ir.sequence.xml',
        'views/account_advance_payment.xml',
        'wizard/account_advance_register_payment.xml',
        'views/acc_type.xml',
    ],
    'images': [
        "static/description/logo.png"
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

