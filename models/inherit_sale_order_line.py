from odoo import fields ,models

class InheritSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    position = fields.Char(string="Position",default="00.00.00")