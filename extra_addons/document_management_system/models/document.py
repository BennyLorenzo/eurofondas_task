from odoo import api, fields, models


class Document(models.Model):
    _name = 'document'
    _description = 'A user added document'

    title = fields.Char(string='Title', required=True)
    description = fields.Char(string = 'Description')
    company = fields.Char(string = 'Company')
    employee = fields.Many2many('employee', string='Responsible employee')