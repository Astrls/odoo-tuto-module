from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate properties"

    name = fields.Char('Property Name', default="Unknown", required=True)
    description = fields.Text('Property Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Availability', copy=False, default=lambda self: fields.Date.add(fields.Date.today(), months=3))
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer('# of bedrooms', default=2)
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('# facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north','North'),('east','East'),('south','South'),('west','West')])

