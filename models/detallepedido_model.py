
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
    total=fields.Float(string="Total",default=0,compute="calculaBase", store=True)
    #precio=fields.Float(string="Precio",compute="precioid", store=True)

    
    @api.depends('productos','cantidad','iva')
    def calculaBase(self):
        for i in self:
            i.base=i.productos.precio*i.cantidad
            i.total = (((i.base*int(i.iva))/100)+i.base)


   

    """@api.depends('productos')
    def precioid(self):
        self.ensure_one()
        self.precio=self.productos.precio"""
   


    