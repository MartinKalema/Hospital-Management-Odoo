from odoo import http


class Hospital(http.Controller):
    @http.route('/patient_webform', type='http', auth='user', website=True)
    def patient_webform(self, **kw):
        return http.request.render('om_hospital.create_patient', {})

    @http.route('/create/webpatient', type='http', auth='user', website=True)
    def create_webpatient(self, **kw):
        http.request.env['hospital.patient'].sudo().create(kw)
        return http.request.render('om_hospital.patient_thanks', {})
