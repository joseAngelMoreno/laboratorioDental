
# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class detallepedido_model(models.Model):

    _name = 'laboratorio_dental.detallepedido_model'

    productos = fields.Many2one("laboratorio_dental.productos_model", "Productos")
    pedidos = fields.Many2one("laboratorio_dental.pedidos_model", "Pedidos")
    cantidad =fields.Integer(string="Cantidad",default=1,equired=True,)    
    iva=fields.Selection(string="IVA",default="0",selection=[("21","21"),("10","10"),("4","4"),("0","0")] )
    base=fields.Float(string="Base",default=0)
    total=fields.Float(string="Total",default=0)
    base=fields.Float(string="Base",default=0,compute="calculaBase", store=True)
    total=fields.Float(string="Total",default=0,compute="calculaTotal", store=True)
    #precio=fields.Float(string="Precio",compute="precioid", store=True)

    @api.depends('productos','cantidad')
    def calculaBase(self):
        self.ensure_one()
        suma = 0
        suma=self.productos.precio*self.cantidad
        self.base = suma


    @api.depends('iva', 'productos','cantidad')
    def calculaTotal(self):
        self.ensure_one()
        self.total = (((self.base*int(self.iva))/100)+self.base)

    """@api.depends('productos')
    def precioid(self):
        self.ensure_one()
        self.precio=self.productos.precio"""
   


    