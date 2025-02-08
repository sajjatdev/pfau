from odoo import api,fields,models,_

class InheritAccountMove(models.Model):
    _inherit ='account.move'

    def invoice_note(self):
        return _(
            " If the payment term is exceeded, 1.5% per month will be charged. The goods remain our property until full payment is received."
        )
   
