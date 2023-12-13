from odoo import models, api, fields


# transcient models don't save data on the database
class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    appointment_id = fields.Many2one('hospital.patient', string='Appointment')
