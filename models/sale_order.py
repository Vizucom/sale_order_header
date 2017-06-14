# -*- coding: utf-8 -*-
from openerp import models, fields, _
import openerp.addons.decimal_precision as dp


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    header_text = fields.Char('Header for Quotation')
