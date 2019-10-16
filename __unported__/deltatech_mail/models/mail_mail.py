# -*- coding: utf-8 -*-
# ©  2015-2019 Deltatech
# See README.rst file on addons root folder for license details

from odoo import _, api, fields, models

from email.utils import formataddr
from odoo.exceptions import UserError


class MailMail(models.Model):
    _inherit = 'mail.mail'

    @api.multi
    def _send_prepare_values(self, partner=None):

        res = super(MailMail, self)._send_prepare_values(partner)

        use_company_email = self.env["ir.config_parameter"].sudo().get_param("mail.use_company_email")
        if use_company_email:
            if self.author_id.company_id.email:
                self.write({'email_from': formataddr((self.author_id.company_id.name, self.author_id.company_id.email))})
            else:
                raise UserError(_("Unable to post message, please configure the company's email address."))

        model = self.model
        if model:
            substitutions = self.env['mail.substitution'].search(['|', ('name', '=', model), ('name', '=', False)])
        else:
            substitutions = self.env['mail.substitution'].search([])

        if substitutions:
            email_to = []
            if model:
                for substitution in substitutions:
                    email_to += [substitution.email]
            else:
                for substitution in substitutions:
                    if substitution in self.message_id:
                        email_to += [substitution.email]
            if email_to:
                res['email_to'] = email_to

        return res
