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

		model_user = http.request.env['res.users']
		id_user =	model_user._uid
		id_member = model_user.search([['id', '=', id_user]])
		mode = http.request.env['membership.point.voucher.setting']
		vouc = mode.search([['is_purchaseable', '=', 'True']])

		return http.request.render('ciptadlab.detail', {
			'id_member' : id_member,
			'id' : id,
			'vouchers' : vouc,
		})

# ==========================================================================================================================

	@http.route('/vouchers/purchase/', auth='user', type='http', website=True)
	def purchase(self, **kw):

		model_member = http.request.env['membership.point.member']
		id_member = model_member.get_member_by_uid()
		member = model_member.serach([['id','=', id_member]])
		model_voucher_setting = http.request.env['membership.point.voucher.setting']
		vouc = model_voucher_setting.search([['id', '=', int(kw[voucher_id]) ]])
		# for o in vouc :
		# 	if()
		mode.purchaseable_member_voucher(vouc, kw['qty'], )

		return http.request.render('ciptadlab.mypurchases', {
			'uid' : id_member,
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