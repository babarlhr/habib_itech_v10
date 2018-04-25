from odoo import api, fields, models, _


class RoleForPurchase(models.Model):
    _inherit = 'stock.picking'

    x_active = fields.Boolean(string="Active",compute="compute_active")
    # active = fields.Boolean(string="Active Two" )

    @api.one
    @api.depends('origin')
    def compute_active(self):
        self.origin
        if 'PO' in self.origin:
            self.x_active = True

