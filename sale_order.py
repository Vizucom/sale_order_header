# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp.tools.translate import _

class sale_order(osv.Model):

    _inherit = 'sale.order'

    _columns = {
        'header_text':            fields.char(_('Header for quotation / sale order'), size=128),
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: