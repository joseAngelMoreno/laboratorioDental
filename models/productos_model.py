
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class productos_model(models.Model):
    _name = 'laboratorio_dental.productos_model'
    _description = 'Modelo de productos'

    name=fields.Char(string="Nombre",required=True)
    descripcion=fields.Html(string="Descripcion",required=True)
    precio=fields.Float(string="Precio",required=True)