# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime,date

class facturas_model(models.Model):
    _name = 'laboratorio_dental.facturas_model'
    _description = 'Modelo de facturas'
    _sql_constraints = [
        ("refPedidoUnico","UNIQUE (ref)","No puede haber dos facturas con la misma referencia!!")]

    ref=fields.Char(string="Referencia" ,required=True,index=True)
    fecha=fields.Date(string="Fecha",  default=date.today())
    iva=fields.Selection(string="IVA",default="21",selection=[("21","21"),("10","10"),("4","4")] )
    base=fields.Float(string="Base",default=0,compute="calculaBase", store=True)
    total=fields.Float(string="Total",default=0,compute="calculaTotal", store=True)
    cliente_id=fields.Many2one("laboratorio_dental.clientes_model","clientes")

    detalleFactura = fields.One2many("laboratorio_dental.detafac_model","facturas_id","detalleFacturas")
    
    active=fields.Boolean(invisible=True,default=True)
    pagada=fields.Boolean(string="Está Pagada?",default=False)


    def cambiaEstado(self):
        self.ensure_one()
        self.pagada = not self.pagada 
        

    def limpiaPagadas(self):
        listaFacturasPagadas=self.search([("pagada","=","True")])
        for factura in listaFacturasPagadas:
            factura.active=False


    @api.depends('detalleFactura')
    def calculaBase(self):
        self.ensure_one()
        suma = 0
        for i in self.detalleFactura:
            suma += i.precios_id.precio*int(i.cantidad)
        self.base = suma

    @api.depends('iva', 'base')
    def calculaTotal(self):
        self.ensure_one()
        self.total = (((self.base*int(self.iva))/100)+self.base)
        
        