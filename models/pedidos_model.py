# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime,date
from odoo.exceptions import ValidationError
class pedidos_model(models.Model):
    _name = 'laboratorio_dental.pedidos_model'
    _description = 'Modelo de pedidos'
    _sql_constraints = [
        ("refPedidoUnico","UNIQUE (ref)","No puede haber dos pedidos con la misma referencia!!")]

    ref=fields.Char(string="Referencia" ,required=True,size=10)
    fechaPedido=fields.Date(string="FechaPedido",  default=date.today())
    iva=fields.Selection(string="IVA",default="21",selection=[("21","21"),("10","10"),("4","4")] )
    base=fields.Float(string="Base",default=0,compute="calculaBase", store=True)
    total=fields.Float(string="Total",default=0,compute="calculaTotal", store=True)
    fechaEntrega=fields.Date(string="FechaEntrega",  default=date.today())
    detallepedido = fields.One2many("laboratorio_dental.detallepedido_model","pedidos","detallePedido")
   


    @api.constrains("fechaEntrega","fechaPedido")
    def compruebaFecha(self):
        if (self.fechaEntrega)<= (self.fechaPedido):
            raise ValidationError("Fecha de entrega debe ser mayor que la fecha de pedido")


    @api.depends('detallepedido')
    def calculaBase(self):
        self.ensure_one()
        suma = 0
        for i in self.detallepedido:
            suma += i.productos.precio*int(i.cantidad)
        self.base = suma

    @api.depends('iva', 'base')
    def calculaTotal(self):
        self.ensure_one()
        self.total = (((self.base*int(self.iva))/100)+self.base)