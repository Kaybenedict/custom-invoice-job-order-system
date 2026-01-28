from odoo import models

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_create_job_order(self):
        self.ensure_one()
        if self.move_type != 'out_invoice':
            return
        lines = []
        for inv_line in self.invoice_line_ids:
            lines.append((0, 0, {
                'product_id': inv_line.product_id.id,
                'description': inv_line.description,
                'height': inv_line.height,
                'width': inv_line.width,
                'unit': inv_line.unit,
                'number_items': inv_line.number_items,
                'total_sq_ft': inv_line.total_sq_ft,
                'amount_per_sq_ft': inv_line.amount_per_sq_ft,
                'total_amount_payable': inv_line.total_amount_payable,
            }))
        job_order = self.env['job.order'].create({
            'invoice_id': self.id,
            'partner_id': self.partner_id.id,
            'line_ids': lines,
        })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'job.order',
            'view_mode': 'form',
            'res_id': job_order.id,
            'target': 'current',
        }