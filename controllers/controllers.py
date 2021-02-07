# -*- coding: utf-8 -*-
# from odoo import http


# class LaboratorioDental(http.Controller):
#     @http.route('/laboratorio_dental/laboratorio_dental/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/laboratorio_dental/laboratorio_dental/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('laboratorio_dental.listing', {
#             'root': '/laboratorio_dental/laboratorio_dental',
#             'objects': http.request.env['laboratorio_dental.laboratorio_dental'].search([]),
#         })

#     @http.route('/laboratorio_dental/laboratorio_dental/objects/<model("laboratorio_dental.laboratorio_dental"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('laboratorio_dental.object', {
#             'object': obj
#         })
