# -*- coding: utf-8 -*-
{
    'name': "Mp POS Extended",

    'summary': """
        Extended POS""",

    'description': """
        Extended POS
    """,
    'author': "TI Department More Products S.A.S",
    'website': "http://www.moreproducts.com",
    'category': 'Sales',
    'version': '0.2.1',
    'depends': [
            'account',
            'base',
            'point_of_sale',
            ],

    'data': [
        'security/ir_security.xml',
        'security/ir.model.access.csv',
        'views/res_company_views.xml',
        'views/pos_config_views.xml',
        #'wizard/wz_state_pos_session_views.xml',
    ],
   'assets': {
        'point_of_sale._assets_pos': [
            'mp_pos_extended/static/src/**/*',
        ],
    },
    
}
