import datetime
from openerp import models, fields, api
from openerp.exceptions import ValidationError

# ==========================================================================================================================

class membership_point_voucher_setting(models.Model):
	_inherit = 'membership.point.voucher.setting'

	voucher_prefix = fields.Char('Voucher Prefix', size=4, required=True)

	@api.constrains('voucher_prefix')
	def _check_voucher_prefix(self):
		for record in self:
			if not record.voucher_prefix.isdigit():
				raise ValidationError('Voucher prefix must be a number.')
			elif len(record.voucher_prefix) != 4:
				raise ValidationError('Voucher prefix must be 4 digits.')

# ==========================================================================================================================

class membership_point_voucher(models.Model):
	_inherit = 'membership.point.voucher'

	def generate_number(self, vals):
		voucher_prefix = self.env['membership.point.voucher.setting'].browse(vals['setting_id'])[0].voucher_prefix
		year = datetime.datetime.now().strftime("%Y")
		voucher_prefix = ('%s%s' % (voucher_prefix, year))

		latest_voucher = self.search([('number', 'like', voucher_prefix)], order="number DESC", limit=1)
		if len(latest_voucher) == 0:
			new_number = "%s00000001" % voucher_prefix
		else:
			latest_voucher = latest_voucher.number[8:]
			new_number = "%s%08d" % (voucher_prefix, int(latest_voucher)+1)

		return new_number