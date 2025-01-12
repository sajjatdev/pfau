from odoo import fields,models,api

class InheritProductAttribute(models.Model):
    _inherit = "product.attribute"

    custom_attr_name = fields.Char(string="Custom Attribute Name", required=True)
    attr_value = fields.Boolean(string="Print On Quotation", default=True)


class InheritProductAttributeValues(models.Model):
    _inherit = "product.attribute.value"

    @api.depends("attribute_id")
    @api.depends_context("show_attribute")
    def _compute_display_name(self):
        if not self.env.context.get("show_attribute", True):
            return super()._compute_display_name()
        for value in self:
            value.display_name = f"{value.attribute_id.custom_attr_name}: {value.name}"
