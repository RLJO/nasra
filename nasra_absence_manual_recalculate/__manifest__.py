# -*- coding: utf-8 -*-
{
    'name': " nasra absence manual recalculate",

    'summary': """""",

    'description': """
    
    """,

    'author': "Centione",
    'website': "www.centione.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','nasra_hr_late_early_absence','nasra_attendance_manual_recalculate'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/recalculate_attendance_wizard_inherit.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}