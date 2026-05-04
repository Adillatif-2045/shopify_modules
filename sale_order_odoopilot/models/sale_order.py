from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_odoopilot = fields.Char(
        string='OdooPilot',
        help='Custom OdooPilot field for Sale Orders',
        tracking=True,
        copy=True,
    )