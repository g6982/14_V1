# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from datetime import date, datetime

class PosSalesSummary(models.TransientModel):

	_name='pos.sale.summary.wizard'
	_description = "POS Sale Summary Wizard"

	start_dt = fields.Date('date de début', required = True)
	end_dt = fields.Date('Date de fin', required = True)
	report_type = fields.Char('Type de rapport', readonly = True, default='PDF')
	only_summary = fields.Boolean('Only Summary')
	res_user_ids = fields.Many2many('res.users', default=lambda s: s.env['res.users'].search([]))

	def sale_summary_generate_report(self):
		return self.env.ref('bi_pos_reports.action_sales_summary_report').report_action(self)
