## KRT Lead Qualification Automation

### 1. Lead Meets Qualification Criteria
`If Lead meets criteris is true then on work completion`
* Set lead_qualified_by to current user
* Set lead_qualified_date to current date(today)
* Change lead Tag from Lead/Dealer/New to Lead/Dealer/Qualified
#### Steps to set Automated Action
* Model -> Contact
* Trigger -> On Save
* Apply On [(lead meets qualification = True),(Qualification Work complete = True)]
* When Updating -> [(Lead meets criteria), (Qualification Work complete)]
#### Create Action
* set type -> Update Record
* Allowed Groups -> [(Adminstration/Access Rights),(User types/Internal Users)]
* Action Detail -> Select Tags -> Setting it to -> Lead/Dealer/Qualified


### 2. Set date on record save
`Is set automatic on record save`
#### Steps to set Automated Action
* Model -> Contact
* Trigger -> On Save
* Apply on -> [(Work complete = True)]
#### Create Action
* Set type -> Execute Code
* If field is datetime`record['x_studio_lead_qualified_date'] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')`
* if field is a date field `record['x_studio_lead_qualified_date'] = datetime.datetime.today()`

### 3. Set Lead to Unqualified when it no longer meets criteria
`If Lead criteria changes to false then set lead to Unqualified`
* Change lead Tag from Lead/Dealer/Qualified to Lead/Dealer/Unqualified
#### Steps to set Automated Action
* Model -> Contact
* Trigger -> On Save
* Apply On [(Lead meets criteria = False)]
#### Create Action
* set type -> Update Record
* Allowed Groups -> [(Adminstration/Access Rights),(User types/Internal Users)]
* Action Detail -> Select Tags -> Setting it to -> Lead/Dealer/Unqualified
