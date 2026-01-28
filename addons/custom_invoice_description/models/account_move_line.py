from odoo import api, fields, models

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    description = fields.Char(string='Description')  # Unchanged
    height = fields.Float(string='Job/H')
    width = fields.Float(string='Job/W')
    unit = fields.Selection([('metres', 'Metres'), ('feet', 'Feet')], string='Unit', default='feet')
    total_sq_ft = fields.Float(string='Total Sq. Ft.', compute='_compute_total_sq_ft', store=True)
    number_items = fields.Float(string='No of Items', default=1.0)
    amount_per_sq_ft = fields.Float(string='Amt/Sq.Ft.', related='price_unit', readonly=True)
    total_amount_payable = fields.Monetary(string='Total Amount Payable', compute='_compute_total_amount', store=True, currency_field='currency_id')

    @api.depends('height', 'width', 'unit')
    def _compute_total_sq_ft(self):
        for line in self:
            if line.unit == 'metres':
                factor = 3.3
                height_ft = line.height * factor
                width_ft = line.width * factor
                line.total_sq_ft = height_ft * width_ft
            else:
                line.total_sq_ft = line.height * line.width

    @api.depends('total_sq_ft', 'price_unit', 'number_items')
    def _compute_total_amount(self):
        for line in self:
            line.total_amount_payable = line.total_sq_ft * line.price_unit * line.number_items

    @api.onchange('height', 'width', 'unit', 'number_items')
    def _onchange_dimensions(self):
        if self.unit == 'metres':
            factor = 3.3
            height_ft = self.height * factor
            width_ft = self.width * factor
            total_sq_ft = height_ft * width_ft
        else:
            total_sq_ft = self.height * self.width
        self.quantity = total_sq_ft * self.number_items