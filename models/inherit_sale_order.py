from odoo import api,fields,models,_

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

    def is_discount(self):
        status = False
        for line in self.order_line:
            if line.discount > 0:
                status = True
        return status

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

    def get_note(self):
        return _(
            "Any product images are representations of the offered model, but not necessarily the chosen variant. Prices are in euros, per unit excluding VAT, valid for the offered quantity."
        )

    def get_text_delivery_time_quot(self):
        return _(
            "Each delivery is subject to the condition that we ourselves are delivered correctly and on time. We cannot be held responsible for delayed deliveries."
        )
    def get_text_delivery_time_sale(self):
        return _(
            "Each delivery is subject to the condition that we ourselves are delivered correctly and on time. We cannot be held responsible for delayed deliveries. Once the goods have arrived in our warehouse, we will promptly contact you to arrange a delivery/order confirmation. The delivery time begins upon order confirmation and the arrival of an agreed deposit. In case of self-collection, the ordered goods must be picked up from our warehouse within 7 days. In case of delayed pick-up, storage costs of €6.00 including VAT per day will apply."
        )

    def get_text_payment_term_note(self):
        return _(
            "If the payment term is exceeded, 1.5% per month will be charged. The goods remain our property until full payment is received."
        )

    def get_text_note_1(self):
        return _(
            "All deliveries are subject to our Terms and Conditions, available at agb.pfau1010.com. We hope that our offer meets your expectations. You can reach us during our business hours at 01 535 40 75 or via email at office@pfau1010.com."
        )
    def get_text_note_2(self):
        return _(
            " We kindly ask for confirmation of the order confirmation under the agreed conditions and for return."
        )
