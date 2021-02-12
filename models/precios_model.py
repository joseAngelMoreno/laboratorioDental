# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class precios_model(models.Model):
    _name = 'laboratorio_dental.precios_model'
    _description = 'Modelo de precios'

    name=fields.Char(string="Nombre",required=True)
    descripcion=fields.Html(string="Descripcion",required=True)
    precio=fields.Float(string="Precio",required=True)
   

    @api.constrains("precio")
    def preciominimo(self):
        self.ensure_one()
        
        if self.precio <= 0:
            raise ValidationError("El precio del producto no puede ser 0")