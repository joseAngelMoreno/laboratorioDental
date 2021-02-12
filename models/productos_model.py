# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class productos_model(models.Model):
    _name = 'laboratorio_dental.productos_model'
    _description = 'Modelo de productos'

    name=fields.Char(string="Nombre",required=True)
    descripcion=fields.Html(string="Descripcion",required=True)
    precio=fields.Float(string="Precio",required=True)
    detallepedido = fields.One2many("laboratorio_dental.detallepedido_model","productos","detallePedidos")
   


    @api.constrains("precio")
    def preciominimo(self):
        self.ensure_one()
        
        if self.precio <= 0:
            raise ValidationError("El precio del producto no puede ser 0")
        