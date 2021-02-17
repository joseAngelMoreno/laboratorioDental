# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime,date

class facturas_model(models.Model):
    _name = 'laboratorio_dental.facturas_model'
    _description = 'Modelo de facturas'
    _sql_constraints = [
        ("refunico","UNIQUE (ref)","No puede haber dos facturas con la misma Referencia!!")]


    #codigo para generar referencia de factura autoincrementable
    ref=fields.Char(string="ID Factura",default=lambda self: self.env['ir.sequence'].next_by_code('incrementa'))
    fecha=fields.Date(string="Fecha",  default=date.today())
    descuento=fields.Selection(string="Descuento ",default="0",selection=[("0","0"),("5","5"),("10","10"),("15","15"),("20","20")] )
    base=fields.Float(string="Base",default=0,compute="calculaBase", store=True)
    total=fields.Float(string="Total",default=0,compute="calculaTotal", store=True)
    cliente_id=fields.Many2one("laboratorio_dental.clientes_model","clientes",required=True)

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


    """@api.depends('detalleFactura')
    def calculaBase(self):
        self.ensure_one()
        suma = 0
        for i in self.detalleFactura:
            suma += i.precios_id.precio*i.cantidad
        self.base = suma"""

      
    @api.depends('detalleFactura')
    def calculaBase(self):
        self.ensure_one()
        suma = 0
        for i in self.detalleFactura:
            suma += i.total
        self.base = suma
    
    
    @api.depends('descuento', 'base')
    def calculaTotal(self):
        self.ensure_one()
        self.total = (self.base-((self.base*int(self.descuento))/100))
        
        