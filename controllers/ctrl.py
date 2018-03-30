from openerp import http
from openerp.exceptions import ValidationError
import re
# ==========================================================================================================================

class Academy(http.Controller):
	

	@http.route('/index/', auth='public', type="http", website=True)
	def index(self, **kw):
		return http.request.render('ciptadlab.index', {
			'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
		})

# ==========================================================================================================================

	@http.route('/home/', auth='user', type="http", website=True)
	def home(self, **kw):
		return http.request.render('ciptadlab.home', {
			'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
		})

# ==========================================================================================================================

	@http.route('/vouchers/', auth='user', type='http', website=True)
	def vouchers(self, **kw):

		uid = http.request.env['membership.point.member'].get_member_by_uid
		mode = http.request.env['membership.point.voucher.setting']
		vouc = mode.search([['is_purchaseable', '=', 'True']])

		return http.request.render('ciptadlab.vouchers', {
			'ids' : uid,
			'vouchers' : vouc,
		})

# ==========================================================================================================================

	@http.route('/vouchers/detail/<int:id>/', auth='user', type='http', website=True)
	def detail(self, id):

		uid = http.request.env['membership.point.member'].get_member_by_uid
		mode = http.request.env['membership.point.voucher.setting']
		vouc = mode.search([['is_purchaseable', '=', 'True']])

		return http.request.render('ciptadlab.detail', {
			'id' : id,
			'vouchers' : vouc,
		})

# ==========================================================================================================================

	@http.route('/vouchers/purchase/', auth='user', type='http', website=True)
	def detail(self, **kw):

		uid = http.request.env['membership.point.member'].get_member_by_uid
		mode = http.request.env['membership.point.voucher.setting']
		vouc = mode.search([['id', '=', id]])
		mode.purchaseable_member_voucher(self, vouc, kw['qty'])

		return http.request.render('ciptadlab.mypurchases', {
			'id' : id,
			'vouchers' : vouc,
		})

# ==========================================================================================================================

	@http.route('/mypurchases/<int:id>/', auth='user', type='http', website=True)
	def mypurchases(self, **kw):

		return http.request.render('ciptadlab.mypurchases', {
			'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
		})

# ==========================================================================================================================

	@http.route('/home/login/', auth='user', type='http', website=True)
	def insert(self, **kw):

		return http.request.render('ciptadlab.home', {
			'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
		})