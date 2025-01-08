from odoo import fields,models,api

class InheritProductAttribute(models.Model):
    _inherit = "product.attribute"

    custom_attr_name = fields.Char(string="Custom Attribute Name", required=True)
    attr_value = fields.Boolean(string="Print On Quotation", default=True)
