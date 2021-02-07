from datetime import datetime,date
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re
class clientes_model(models.Model):
    _name = 'laboratorio_dental.clientes_model'
    _description = 'Modelo de clientes'

    name=fields.Char(string="Nombre",required=True)
    nif=fields.Char(string="NIF del cliente",required=True,index=True)
    cliente_id=fields.Char(string="Cliente id",required=True)
    poblacion=fields.Char(string="Poblacion",required=True)
    email=fields.Char(string="Email")
    telefono=fields.Char(string="Telefono",required=True,size=9)
    foto=fields.Binary(string="Foto")

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





    @api.constrains("nif")
    def checkNif(self):
        if len(self.nif)>9 or len(self.nif)<9:
            raise ValidationError("El Nif debe contener 9 caracteres")
        else:
            num = self.nif[1:]
            letra=self.nif[0].upper()

            if not letra.isalpha():
                raise ValidationError("El primer caracter debe ser letra")
            if not letra.isupper():
                raise ValidationError("La letra debe estar en mayúsculas")
            else:
                if not num.isdigit():
                    raise ValidationError("los ultimos 8 deben ser numeros")
                return self.nif
                    
               