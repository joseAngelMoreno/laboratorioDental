# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class detaFac_model(models.Model):

    _name = 'laboratorio_dental.detafac_model'

    facturas_id = fields.Many2one("laboratorio_dental.facturas_model", "Factura")
    precios_id = fields.Many2one("laboratorio_dental.precios_model", "Nombre del producto")
    cantidad =fields.Selection(string="Cantidad",selection=[("1","1"),("2","2"),("3","3"),("4","4"),("5","5")] )
    
   


    
        
        
        
        
        
        
        
        
        
        
        
    