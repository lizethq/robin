# -*- coding: utf-8 -*-

from odoo import models, fields, api, SUPERUSER_ID, _
from odoo.exceptions import ValidationError
import time
import json
import logging

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'purchase.requisition'
    
    
    def action_approve_lines(self):
        raise UserError(_('action_approve_lines'))
        
    
    def action_reject_lines(self):
        raise UserError(_('action_reject_lines'))

    