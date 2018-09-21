# -*- coding: utf-8 -*-
# ©  2008-2018 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details

from odoo.addons.point_of_sale.wizard.pos_box import PosBox
from odoo import models, fields, api, _
from odoo.exceptions import UserError
import base64
from io import StringIO

"""
Introducere numerar in sertar :
I,1,______,_,__;0;10<suma>;;;;

Retragere numerar din sertar :
I,1,______,_,__;1;10<suma>;

I,1,______,_,__;0;1000;tr;;;
P,1,______,_,__;dispozitie de incasare nr.235/20.09.2018;;;;
P,1,______,_,__;S-a incasat de la delegat...............;;;;
P,1,______,_,__;suma de: 1000.00 lei ;;;;
P,1,______,_,__;reprezentand ...........................;;;;
P,1,______,_,__;---------------------------------------;;;;
P,1,______,_,__;---------------------------------------;;;;
P,1,______,_,__;Am primit--------   -----Am predat;;;;
P,1,______,_,__;Violeta Vasilescu--------Popescu Ciprian;;;;
P,1,______,_,__;---------------------------------------;;;;
P,1,______,_,__;---------------------------------------;;;;
P,1,______,_,__;---------------------------------------;;;;
P,1,______,_,__;---------------------------------------;;;;
P,1,______,_,__;---------------------------------------;;;;

"""

class PosBoxExtended(PosBox):
    _register = False

    #file_name = fields.Char(string='File Name')
    #data_file = fields.Binary(string='File')
    partner_id = fields.Many2one('res.partner', string='Partner')
    number = fields.Char("Number",  default=lambda self: self.env['ir.sequence'].next_by_code('pos.box'))

    @api.one
    def _create_bank_statement_line(self, record):
        res = super(PosBoxExtended, self)._create_bank_statement_line(record)
        return res

    # @api.multi
    # def do_download_file(self):
    #     return {
    #         'type': 'ir.actions.act_url',
    #         'url': '/web/content?model=%s&download=True&field=data_file&id=%s&filename=%s' % (
    #         self._name, self.id, self.file_name),
    #         'target': 'self',
    #     }

    def print_bf_in_out(self,type, record):
        com_print = 'P,1,______,_,__;%s;;;;\r\n'
        if type == 'in':
            com = 'I,1,______,_,__;1;%s;;;;\r\n'
            txt1 = _('Cash collection')
            txt2 = _('It has been collected from the delegate')
            txt3 = self.env.user.name
            if self.partner_id:
                txt3 += '          '+self.partner_id.name

        if type == 'out':
            com = 'I,1,______,_,__;0;%s;;;;\r\n'
            txt1 = _('Payment disposal')
            txt2 = _('It was paid to the delegate')
            txt3 = ''
            if self.partner_id:
                txt3 += self.partner_id.name
            txt3 += '          ' + self.env.user.name


        amount = self.amount
        amount = -amount if amount < 0.0 else amount
        data_file = ''
        data_file += com % amount
        data_file += com_print % ('%s :%s' % ( txt1, self.number))
        data_file += com_print % '---------------------------------------'
        data_file += com_print % txt2
        data_file += com_print % (_('amount :%s') % amount)
        data_file += com_print % ('Ref :%s' % self.name or '')
        data_file += com_print % '---------------------------------------'
        data_file += com_print % '---------------------------------------'

        data_file += com_print % 'I received,            I gave,'
        data_file += com_print % txt2

        data_file += com_print % '---------------------------------------'
        data_file += com_print % '---------------------------------------'
        data_file += com_print % '---------------------------------------'
        data_file += com_print % '---------------------------------------'
        data_file += com_print % '---------------------------------------'
        data_file = base64.encodestring(data_file.encode())
        wizard = self.env['wizard.download.file'].create({'data_file': data_file, 'file_name': 'cash_box_in.inp'})
        #self.write({'data_file': data_file, 'file_name': 'cash_box_in.inp'})

        return wizard.do_download_file()


class PosBoxIn(PosBoxExtended):
    _inherit = 'cash.box.in'

    def _calculate_values_for_statement_line(self, record):
        values = super(PosBoxIn, self)._calculate_values_for_statement_line(record=record)
        if self.partner_id:
            values['partner_id'] = self.partner_id.id
        values['name'] =  self.number
        values['ref'] = _('Put Money In Cash')
        return values


    @api.multi
    def run(self):
        active_model = self.env.context.get('active_model', False)
        active_ids = self.env.context.get('active_ids', [])
        res = super(PosBoxIn, self).run()
        if active_model == 'pos.session':
            record = self.env[active_model].browse(active_ids)
            res=self.print_bf_in_out('in',record)
        return res


class PosBoxOut(PosBoxExtended):
    _inherit = 'cash.box.out'

    ref = fields.Char('Reference')

    def _calculate_values_for_statement_line(self, record):
        values = super(PosBoxOut, self)._calculate_values_for_statement_line(record=record)
        if self.partner_id:
            values['partner_id'] = self.partner_id.id
        values['name'] = self.number
        values['ref'] = _('Put Money In Cash')
        return values


    @api.multi
    def run(self):
        active_model = self.env.context.get('active_model', False)
        active_ids = self.env.context.get('active_ids', [])
        res = super(PosBoxOut, self).run()
        if active_model == 'pos.session':
            record = self.env[active_model].browse(active_ids)
            res = self.print_bf_in_out('out', record)
        return res


