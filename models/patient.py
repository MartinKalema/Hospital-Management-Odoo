from odoo import api, fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"  # Table name will be hospital_patient.
    _inherit = ['mail.thread', 'mail.activity.mixin']  # adding chatter to form
    _description = "Hospital patient"

    # By default, the _rec_name of a model is the 'name' field.
    name = fields.Char(string='Name', tracking=True, required=True)
    ref = fields.Char(string='Reference', tracking=True, help='Patient unique identifier', required=True)
    # computed fields are not automatically stored in the database, you have to use 'store=True'
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True, required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True, required=True)
    active = fields.Boolean(string='Active', default=True, tracking=True)
    date_of_birth = fields.Date(string='Date of Birth', tracking=True, required=True)
    # Create another action with a treeView to show all the appointments a patient has.
    appointment_id = fields.Many2one('hospital.appointment', string='Appointments')
    image = fields.Image(string='Image')
    tag_ids = fields.Many2many('patient.tag', string='Tags')

    # Whenever date of birth changes, the _compute_age() is executed.
    # The value is computed before saving, so you see the age change immediately.
    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        # check out the singleton error. We iterate to avoid the singleton error
        for record in self:
            if record.date_of_birth:
                record.age = today.year - record.date_of_birth.year
            # the else statement is a must, otherwise you will get errors. The computed field must always have a value.
            else:
                record.age = 0
