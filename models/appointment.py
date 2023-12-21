from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"  # Table name will be hospital_patient.
    _inherit = ['mail.thread', 'mail.activity.mixin']  # adding chatter to form
    _description = "Hospital appointment"
    # We don't have a name field, hence we need to state the _rec_name.
    _rec_name = "patient_id"

    # manyToOne fields end with _id
    patient_id = fields.Many2one('hospital.patient', string='Patient', tracking=True, required=True)
    appointment_time = fields.Datetime(string='Appointment time', default=fields.Datetime.now, tracking=True, required=True)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today, tracking=True, required=True)
    # related field, 'readonly=False' to make changes
    gender = fields.Selection(related='patient_id.gender', required=True)
    ref = fields.Char(string='Reference', tracking=True, required=True)
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Urgent'),
    ], string='Priority', default='0', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('canceled', 'Cancelled'),
    ], string='Status', default='draft', required=True)
    doctor_id = fields.Many2one('res.users', string='Doctor', required=True)
    # In a One-to-many relation, we end the field name with 'ids'
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string='Pharmacy Lines')
    hide_sales_price = fields.Boolean(string='Hide sales price')

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    @staticmethod
    def action_test(self):
        # print('Button clicked!!!!!!!!!!!!!!')
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'clicked successfully',
                'type': 'rainbow_man',
            }
        }

    @staticmethod
    def action_in_consultation(self):
        for record in self:
            record.state = 'in_consultation'

    @staticmethod
    def action_done(self):
        for record in self:
            record.state = 'done'

    @staticmethod
    def action_cancel(self):
        return self.env.ref('om_hospital.action_cancel_appointment').read()[0]
        # for record in self:
        #     record.state = 'canceled'

    @staticmethod
    def action_draft(self):
        for record in self:
            record.state = 'draft'


class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmacy Lines"

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price')
    qty = fields.Integer(string='Quantity', default='1')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')