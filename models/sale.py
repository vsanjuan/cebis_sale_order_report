# -*- coding: utf-8 -*-

from openerp import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    non_valued_do = fields.Boolean('Non-valued delivery order', default=False)
