from odoo import api,fields,models

class InheritPartner(models.Model):

     _inherit ='res.partner'

     is_vandor = fields.Boolean(string="Is Vandor",default=False)
     supplier_discount = fields.Float(string="Supplier Discount",default=0.0)