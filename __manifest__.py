# -*- coding: utf-8 -*-
{
    'name': "laboratorioDental",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Jose Angel",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/laboratorio_security.xml',
        'security/ir.model.access.csv',
        'views/trabajadores_view.xml',
        'views/clientes_view.xml',
        'views/precios_view.xml',
        'views/pedidos_view.xml',
        'views/productos_view.xml',
        'views/facturas_view.xml',
        'views/detafac_view.xml',
        'views/detallepedido_view.xml',
        'views/menu.xml'
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
    'installable':True,
}
