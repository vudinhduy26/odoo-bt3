# -*- coding: utf-8 -*-
# from odoo import http


# class BusinessPlanManagers(http.Controller):
#     @http.route('/business_plan_managers/business_plan_managers', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/business_plan_managers/business_plan_managers/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('business_plan_managers.listing', {
#             'root': '/business_plan_managers/business_plan_managers',
#             'objects': http.request.env['business_plan_managers.business_plan_managers'].search([]),
#         })

#     @http.route('/business_plan_managers/business_plan_managers/objects/<model("business_plan_managers.business_plan_managers"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('business_plan_managers.object', {
#             'object': obj
#         })
