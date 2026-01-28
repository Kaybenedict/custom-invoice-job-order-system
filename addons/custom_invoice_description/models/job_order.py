from odoo import api, fields, models

class JobOrder(models.Model):
    _name = 'job.order'
    _description = 'Job Order'

    name = fields.Char(string='Reference', default='New', readonly=True)
    invoice_id = fields.Many2one('account.move', string='Invoice')
    partner_id = fields.Many2one('res.partner', string='Customer')
    date = fields.Date(string='Date', default=fields.Date.today)
    line_ids = fields.One2many('job.order.line', 'job_order_id', string='Lines')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('job.order') or 'New'
        return super().create(vals)

class JobOrderLine(models.Model):
    _name = 'job.order.line'
    _description = 'Job Order Line'

    job_order_id = fields.Many2one('job.order')
    product_id = fields.Many2one('product.product', string='Product')
    description = fields.Char(string='Description')
    height = fields.Float(string='Job/H')
    width = fields.Float(string='Job/W')
    unit = fields.Selection([('metres', 'Metres'), ('feet', 'Feet')], string='Unit')
    number_items = fields.Float(string='No of Items')
    total_sq_ft = fields.Float(string='Total Sq. Ft.')
    amount_per_sq_ft = fields.Float(string='Amt/Sq.Ft.')
    total_amount_payable = fields.Monetary(string='Total Amount Payable', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', related='job_order_id.invoice_id.currency_id')