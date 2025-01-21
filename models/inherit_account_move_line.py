from odoo import api,fields,models

class InheritAccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    position = fields.Char(string="Position", default="00.00.00")
