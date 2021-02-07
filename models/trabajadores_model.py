# -*- coding: utf-8 -*-
from datetime import datetime,date
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re
class trabajadores_model(models.Model):
    _name = 'laboratorio_dental.trabajadores_model'
    _description = 'Modelo de trabajadores'


    _sql_constraints = [
        ("numEmpleadoUnico","UNIQUE (numEmpleado)","No puede haber dos trabajadores con el mismo numero de empleado!!"),
        ("dniUnico","UNIQUE (dni)","No puede haber dos trabajadores con el mismo Dni!!")]


    name=fields.Char(string="Nombre",required=True)
    apellidos=fields.Char(string="Apellidos",required=True)
    numEmpleado=fields.Integer(string="NumEmpleado",required=True,index=True)
    dni=fields.Char(string="DNI",required=True,index=True,size=9)
    edad=fields.Integer(string="Edad",required=True)
    fechaAlta=fields.Date(string="FechaAlta",default=lambda self:date.today(),required=True)
    poblacion=fields.Char(string="Poblacion",required=True)
    email=fields.Char(string="Email")
    telefono=fields.Char(string="Telefono",required=True,size=9)
    foto=fields.Binary(string="Foto")

    @api.constrains("edad")
    def esMayor(self):
        if self.edad<16:
            raise ValidationError("Debe tener al menos 16 años")


    @api.constrains("email")
    def es_correo_valido(self):
        expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        comprueba= re.match(expresion_regular, self.email) is not None
        if comprueba==False:
            raise ValidationError("Formato de correo no valido")

    @api.constrains("telefono")
    def telefonoCorrecto(self):
        
        if len(self.telefono)>9 or len(self.telefono)<9:
            raise ValidationError("telefono tiene que tener 9 digitos")
        else:
            if self.telefono.isdigit():
                None
            else:
                raise ValidationError("telefono no puede tener letras")


    @api.constrains("dni")
    def checkDni(self):
        letras="TRWAGMYFPDXBNJZSQVHLCKE"

        if len(self.dni)>9 or len(self.dni)<9:
            raise ValidationError("debe contener 9 caracteres")
        else:
            num = self.dni[:-1]
            if num.isdigit():
                letra = self.dni[-1]
                if letra.isalpha():
                    letra=letra.upper()
                    num = int(num)
                    posicion = num%23
                    if letra!=letras[posicion]:
                        raise ValidationError("El Dni no es valido")
                    
                else:
                    raise ValidationError("el ultimo caracter debe ser una letra")
            else:
                raise ValidationError("los primeros 8 deben ser numeros")
                  

