
from odoo.exceptions import ValidationError




nif="f4438364g"
num = nif[1:]
letra=nif[0]

if num.isdigit():
    if letra.isalpha():
        print("numero correcto")
    else:
        print("El primer caracter debe ser letra")
else:
    print("los ultimos 8 deben ser numeros")


            

    