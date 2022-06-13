# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from datetime import date, datetime

class PosProfitLoss(models.TransientModel):

	_name='pos.profit.loss.wizard'
	_description = "POS Profit Loss Wizard"

	start_dt = fields.Date('date de début', required = True)
	end_dt = fields.Date('Date de fin', required = True)
	
	
	def pos_profit_loss_report(self):
		return self.env.ref('bi_pos_reports.action_profit_loss_report').report_action(self)
