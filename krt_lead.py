# dependencies
x_studio_type,x_studio_is_reseller,x_studio_business_google_url,x_studio_business_google_star_rating,x_studio_exterior_photo_is_commercial,x_studio_not_a_gearfire_or_vector_website,x_studio_not_a_corporate_business


# compute
for record in self:
    if record.x_studio_type != 'Other' and record.x_studio_is_reseller and record.x_studio_business_google_url and record.x_studio_business_google_star_rating >= 3.2 and record.x_studio_exterior_photo_is_commercial and record.x_studio_not_a_gearfire_or_vector_website and x_studio_not_a_corporate_business:
        record['x_studio_lead_meets_qualification_criteria'] = True
    else:
        record['x_studio_lead_meets_qualification_criteria'] = False
