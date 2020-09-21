# ©  2015-2019 Deltatech
# See README.rst file on addons root folder for license details

{
    "name": "Deltatech Sale Margin",
    "version": "11.0.1.0.0",
    "category": "Sales Management",
    "author": "Dorin Hongu",
    "website": "",
    "depends": ["sale_margin", "account", "l10n_ro_invoice_report"],
    "license": "AGPL-3",
    "data": [
        "security/sale_security.xml",
        "security/ir.model.access.csv",
        "views/sale_margin_view.xml",
        "views/account_invoice_view.xml",
        "report/sale_margin_report.xml",
        "views/commission_users_view.xml",
        "wizard/commission_compute_view.xml",
        "wizard/update_purchase_price_view.xml",
    ],
    "images": ["static/description/main_screenshot.png"],
    "active": False,
    "installable": True,
}
