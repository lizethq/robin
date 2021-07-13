# -*- coding: utf-8 -*-
{
    'name': "purchase_requisition_extended",
        
    'version': '13.1',

    'author': "Todoo SAS",

    'contributors': ['Luis Felipe Navas ln@todoo.co'],

    'website': "www.todoo.co",

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase_requisition'],

    # always loaded
    'data': [        
        'views/purchase_requisition_view.xml'
        
    ],
    
    'installable': True    
}
