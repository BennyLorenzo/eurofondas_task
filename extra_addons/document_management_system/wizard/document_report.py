from odoo import api, fields, models


class DocumentReportWizard(models.TransientModel):
    _name = "document.report.wizard"
    _description = "Print Document Report Wizard"

    employee_id = fields.Many2many('employee', string='Employee')
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    def action_print_report(self):
        documents = self.env['document'].search_read([])
        data = {
            'form':self.read()[0],
            'documents': documents
        }
        return self.env.ref('document_management_system.action_report_documents').report_action(self, data=data)