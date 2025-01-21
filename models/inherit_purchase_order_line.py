from odoo import fields,models

class InheritPurchaseOrder(models.Model):
    _inherit = 'purchase.order.line'

    position = fields.Char(string="Position", default="00.00.00")
