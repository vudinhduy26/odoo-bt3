# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class business_plan_managers(models.Model):
#     _name = 'business_plan_managers.business_plan_managers'
#     _description = 'business_plan_managers.business_plan_managers'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
