# -*- coding: utf-8 -*-

from odoo import models, fields, api, SUPERUSER_ID, _
from odoo.exceptions import ValidationError, UserError
import time
import json
import logging

_logger = logging.getLogger(__name__)


class PurchaseRequisition(models.Model):
    _inherit = 'purchase.requisition'
    
    nueva_var = fields.Char('Tipo de documento', default='')
    
    
    def action_open(self):
        if self.env.user == self.x_studio_account_analytic_ids.x_studio_user_id:
            self.write({'state': 'open'})
        else:
            raise UserError(_('NOOOOOOOOO'))
        
    
    
    def action_approve_lines(self):
        raise UserError(_('action_approve_lines'))
        
    
    def action_reject_lines(self):
        raise UserError(_('action_reject_lines'))

    