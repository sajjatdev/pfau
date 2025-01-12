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

    delivery_term_quot = fields.Text(
        string="Delivery Terms",
        default="Frei Haus Wien, inkl. Vertragen, Montage und Entsorgen des Verpackungsmaterials",
    )
    delivery_term_sale = fields.Text(
        string="Delivery Terms",
        default="Frei Haus Wien, inkl. Vertragen, Montage und Entsorgen des Verpackungsmaterials",
    )

    delivery_time_quot = fields.Text(
        string="Expected Delivery Weeks", default="5-7 Wochen ab Auftragsklarheit"
    )
    delivery_time_sale = fields.Text(
        string="Expected Delivery Weeks", default="5-7 Wochen ab Auftragsklarheit"
    )

    def state_status(self):
        for record in self:
            pass
        return False

    def show_tax(self):
        # Dictionary to group taxes by percentage
        tax_groups = {}
        total_price = 0.0

        # Iterate through the order lines to calculate total price and group taxes
        for line in self.order_line:
            # Add the price (including taxes) to the total
            total_price += line.price_total

            # Process each tax associated with the order line
            if line.tax_id:
                for tax in line.tax_id:
                    # Group taxes by their rate
                    tax_rate = tax.invoice_label  # Tax percentage (e.g., 10% or 20%)
                    tax_amount = line.price_tax  # Amount of tax applied on the line

                    # Create a group for this tax rate if it doesn't exist yet
                    if tax_rate not in tax_groups:
                        tax_groups[tax_rate] = {
                            "tax_amount": 0.0,  # Total tax amount for this rate
                            "description": f"{tax_rate}",
                        }

                    # Add the current tax amount to the group
                    tax_groups[tax_rate]["tax_amount"] += tax_amount

        # Prepare tax groups summary
        tax_summary = []
        for rate, data in tax_groups.items():
            tax_summary.append(f"{data['description']} Mwst. ")

        # Return a summary of taxes and total price
        return {"tax_groups": tax_summary, "total_price": total_price}
