from odoo import fields ,models
from odoo.fields import Command

class InheritSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    position = fields.Char(string="Position",default="00.00.00")

    def _prepare_invoice_line(self, **optional_values):

        self.ensure_one()

        res = super(InheritSaleOrderLine, self)._prepare_invoice_line(**optional_values)

        res["position"] = self.position

        print(res)
        
        if optional_values:
            res.update(optional_values)

        return res
