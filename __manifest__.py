{
    'name': "CRM Average",
    'version': "1.0",
    'description': """
    An Application to calculate lead quality""",
    'author': "mugo",
    'category': "CRM",
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "views/average_views.xml",
        "views/average_menu.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': "LGPL-3",
}