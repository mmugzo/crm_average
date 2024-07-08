# dependencies field
dependencies = x_studio_average_score, 
                x_studio_p65_eos_life, 
                x_studio_p65_know_like_trust,
                x_studio_p65_location_independent,
                x_studio_p65_no_inventory
                x_studio_p65_monthly_income,
                x_studio_p65_long_term_income
    
# computed field
for record in self:
    record['x_studio_average_score'] = (int(record.x_studio_p65_eos_life) + int(record.x_studio_p65_know_like_trust) + int(record.x_studio_p65_location_independent) + int(record.x_studio_p65_no_inventory) + int(record.x_studio_p65_monthly_income) + int(record.x_studio_p65_long_term_income)) / 6
