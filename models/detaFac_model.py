# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class detaFac_model(models.Model):

    _name = 'laboratorio_dental.detafac_model'

    facturas_id = fields.Many2one("laboratorio_dental.facturas_model", "Factura")
    precios_id = fields.Many2one("laboratorio_dental.precios_model", "Producto")
    cantidad =fields.Integer(string="Cantidad",default=1,required=True)
    iva=fields.Selection(string="IVA",default="0",selection=[("21","21"),("10","10"),("4","4"),("0","0")] )
    base=fields.Float(string="Base",default=0,compute="calculaBase", store=True)
    total=fields.Float(string="Total",default=0,compute="calculaBase", store=True)
    precio=fields.Float(string="Precio Unidad",compute="calculaBase", store=True)



    #esto no me lo hace en el form de factura
    @api.depends('precios_id','cantidad','iva')
    def calculaBase(self):
        for i in self:
            i.base=i.precios_id.precio*i.cantidad
            i.total = (((i.base*int(i.iva))/100)+i.base)

            #solo para mostrar el precio del producto al crear una linea de detalle
            i.precio=i.precios_id.precio

    



  


    
        
        
        
        
        
        
        
        
        
        
        
    