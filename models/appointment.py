from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"  # Table name will be hospital_patient.
    _inherit = ['mail.thread', 'mail.activity.mixin']  # adding chatter to form
    _description = "Hospital appointment"
    # We don't have a name field, hence we need to state the _rec_name.
    _rec_name = "patient_id"

    # manyToOne fields end with _id
    patient_id = fields.Many2one('hospital.patient', string='Patient', tracking=True)
    appointment_time = fields.Datetime(string='Appointment time', default=fields.Datetime.now, tracking=True)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today, tracking=True)  # Date today
    gender = fields.Selection(related='patient_id.gender')  # related field, 'readonly=False' to make changes
    ref = fields.Char(string='Reference', tracking=True)
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Urgent'),
    ], string='Priority', default='0')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('canceled', 'Cancelled'),
    ], string='Status', default='draft', required=True)

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    @staticmethod
    def action_test(self):
        print('Button clicked!!!!!!!!!!!!!!')
