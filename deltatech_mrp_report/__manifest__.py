# -*- coding: utf-8 -*-
# ©  2015-2018 Deltatech
# See README.rst file on addons root folder for license details
{
    "name": "Deltatech MRP Report",
    "version": "1.0",
    "author": "Terrabit, Dorin Hongu",
    "website": "www.terrabit.ro",
    "description": """

Functionalitati:
 
 - Raport de productie centralizat pe interval
 

    """,

    "category": "Manufacturing",
    "depends": [
        "stock",
        "date_range"

    ]
    ,

    "data": [
        'views/product_view.xml',
        'wizard/mrp_summary_view.xml',
        'views/mrp_summary_template.xml'
    ],
    "images": ['images/main_screenshot.png'],

    "active": False,
    "installable": True,
}
