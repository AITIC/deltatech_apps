# -*- coding: utf-8 -*-
# ©  2008-2020 Terrabit
# See README.rst file on addons root folder for license details

{
    "name": "Analytic account split",
    'version': '12.0.2.0.0',
    "author": "Terrabit, Dan Stoica",
    "website": "https://www.terrabit.ro",
    "category": "Accounting & Finance",
    "depends": [
        "account",
        "analytic",
    ],
    'summary': 'Split analytic line into multiple lines',

    "license": "AGPL-3",
    "data": [
        "wizard/analytic_split.xml",
    ],
    'application': True,
    "active": False,
    "installable": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
