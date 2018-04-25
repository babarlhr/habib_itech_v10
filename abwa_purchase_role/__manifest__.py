# -*- coding: utf-8 -*-
{
    'name': "Purchase Role",

    'summary': """Employee, Applicant Module Customized Form""",

    'description': """
        Modified form of Employee and Applicant Module:

    """,

    'author': "Itech",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase'],

    'data': [
        'security/abwa_purchase_role.xml',
        # 'security/ir.model.access.csv',
        'views/view.xml',

    ],


    # always loaded

    # only loaded in demonstration mode
    'demo': [

    ],
}