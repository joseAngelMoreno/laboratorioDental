# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime,date

class facturas_model(models.Model):
    _name = 'laboratorio_dental.facturas_model'
    _description = 'Modelo de facturas'
    _sql_constraints = [
        ("refPedidoUnico","UNIQUE (ref)","No puede haber dos facturas con la misma referencia!!")]

    ref=fields.Char(string="Referencia" ,required=True)
    fecha=fields.Date(string="Fecha",  default=date.today())
    iva=fields.Selection(string="IVA",default="21",selection=[("21","21"),("10","10"),("4","4")] )
    base=fields.Float(string="Base",default=0)
    total=fields.Float(string="Total",default=0)