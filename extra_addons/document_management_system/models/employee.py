from odoo import api, fields, models


class Employee(models.Model):
    _name = 'employee'
    _description = 'An employee responsible for a document'

    name = fields.Char(string = 'Name', required=True)