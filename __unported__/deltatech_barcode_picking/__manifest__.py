# -*- coding: utf-8 -*-
# ©  2008-2018 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details

{
    "name": "Deltatech Barcode Picking",
    'version': '11.0.1.0.0',
    "author": "Terrabit, Dorin Hongu",
    "website": "www.terrabit.ro",

    'category': 'Warehouse',

    "depends": ["stock",'barcodes'],

    "description": """
Features:    
 - Add product to picking using barcode scanner
 
""",
    "data": [
        'views/picking_views.xml',
        'views/stock_inventory_view.xml'
    ],
    "active": False,
    "installable": True,

}
