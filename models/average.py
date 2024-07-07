from odoo import models, fields, api

RATING_SCORES = [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ]

class LeadQuality(models.Model):
    _name = 'lead.quality'
    _description = 'Lead Quality'

    eos_life = fields.Selection(RATING_SCORES,string='P65 EOS Life', default=0)
    trust = fields.Selection(RATING_SCORES,string='P65 Know,Like,Trust', default=0)
    location = fields.Selection(RATING_SCORES,string='P65 Location Independent', default=0)
    inventory = fields.Selection(RATING_SCORES,string='P65 No Inventory', default=0) 
    monthly_income = fields.Selection(RATING_SCORES,string='P65 Monthly Income', default=0)
    long_term_income = fields.Selection(RATING_SCORES,string='P65 Long Term Income', default=0)
    scoring_avg = fields.Float(string='P65 Score', compute='_compute_scoring', store=True)

    @api.depends('eos_life', 'trust', 'location', 'inventory', 'monthly_income', 'long_term_income')
    def _compute_scoring(self):
        for record in self:
            record.scoring_avg = (int(record.eos_life) + int(record.trust) + int(record.location) + int(record.inventory) + int(record.monthly_income) + int(record.long_term_income)) / 6
