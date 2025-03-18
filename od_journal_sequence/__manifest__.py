# -*- coding: utf-8 -*-
# Copyright 2024 NIMBUTECH S.A.S

{
    'name': 'secuencias de los diarios para  Odoo 17 nbt',
    'version': '17.0',
    'category': 'Accounting',
    'summary': 'secuencias de los diarios para  Odoo 17',
    'description': 'secuencias de los diarios para  Odoo 17',
    "author" : "NIMBUTECH S.A.S",
    "email": 'desarrollo.odoo@nimbutech.com',
    "website":'https://www.nimbutech.com/',
    'depends': ['account'],
    'demo': [],
    'data': [
        'data/account_data.xml',
        'views/account_journal.xml',
        'views/account_move.xml',
    ],
    'qweb': [],
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/banner.png'],
}
