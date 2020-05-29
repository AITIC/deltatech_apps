# -*- coding: utf-8 -*-
# ©  2015-2020 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details

from odoo import api, models, fields


class ProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    condition = fields.Selection([('new', 'New'), ('refurbish', 'Refurbish'), ('broken', 'Broken')], default='new')
    discount = fields.Float()


