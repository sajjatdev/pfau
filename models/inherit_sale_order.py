from odoo import api,fields,models

class InheritSaleOrder(models.Model):
    _inherit = "sale.order"

    sale_subject = fields.Text(
        string="Sale Default Subject For Quotation",
    )

    sale_order_subject = fields.Text(
        string="Sale Default Subject For Quotation",
    )

    cover_note_sale = fields.Text(
        string="Cover Note Sale",
        default="Wir danken für die Einladung zur Anbotslegung und bieten unter Berücksichtigung unserer Verkaufsbedingungen an:",
    )

    cover_note_quot = fields.Text(
        string="Cover Note Quotation",
        default="Wir danken für die Einladung zur Anbotslegung und bieten unter Berücksichtigung unserer Verkaufsbedingungen an:",
    )

    delivery_term = fields.Text(
        string="Delivery Terms",
        default="Frei Haus Wien, inkl. Vertragen, Montage und Entsorgen des Verpackungsmaterials",
    )

    delivery_time = fields.Text(
        string="Expected Delivery Weeks", default="5-7 Wochen ab Auftragsklarheit"
    )

    def get_discounts(self):
        for order in self:
            # Retrieve all related discount records
            discount_records = self.env["sale.order.discount"].search(
                [("sale_order_id", "=", order.id)]
            )
            return discount_records
