
# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class detallepedido_model(models.Model):

    _name = 'laboratorio_dental.detallepedido_model'

    productos = fields.Many2one("laboratorio_dental.productos_model", "Productos")
    pedidos = fields.Many2one("laboratorio_dental.pedidos_model", "Pedidos")
    cantidad =fields.Selection(string="Cantidad",default="1",selection=[("1","1"),("2","2"),("3","3"),("4","4"),("5","5")] )