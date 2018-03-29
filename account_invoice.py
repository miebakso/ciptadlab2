from openerp import models, fields, api, _
from openerp.osv import osv, fields
import re
from datetime import datetime, timedelta, date
from openerp import tools, SUPERUSER_ID
import base64, csv, StringIO

class account_invoice(osv.osv):
	
	_inherit = 'account.invoice'
	
	@api.multi
	def confirm_paid(self):
		super(account_invoice, self).confirm_paid()
	# ketika invoice dibayar, set tanggal bayarnya yaitu tanggal payment pertama
		payment_date = date.today()
		for payment in self.payment_ids:
			if payment.date:
				payment_date = payment.date
			elif payment.date_created:
				payment_date = payment.date_created
			break # ambil payment yang pertama aja. asumsi tidak ada backdate payment sedemikian sehingga tanggal payument yang kedua lebih dulu dari yang pertama
		return self.write({'payment_date': payment_date})
		
	@api.model
	def calculate_invoice_point(self, member, invoice_line):
	# ambil nilai uang dari mo ini
		amount = invoice_line.price_subtotal
	# ambil settingan terakhir. kalau productnya ngga ada setting, ya udah
		setting = invoice_line.product_id.member_point_settings
		if not setting: return 0
	# dapatkan setting line berdasarkan level member saat ini 
		used_setting_line = None
		for setting_line in setting:
			if setting_line.membership_level_id.id == member.current_level.id:
				used_setting_line = setting_line
				break
		if not used_setting_line: return 0
	# hitung poin beserta pembulatannya
		point = used_setting_line.factor * amount / 1000		
		point = point - (point % used_setting_line.rounding)
		return point


