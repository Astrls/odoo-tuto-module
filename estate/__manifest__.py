{
    'name': "AS Real Estate",
    'version': '1.0',
    'depends': ['base'],
    'installable': True,
    'application': True,
    'author': "Antoine",
    'data': [
        'security/ir.model.access.csv',
        'views/estate_menus.xml',
        'views/estate_property_views.xml',
        ],
    #'category': 'Category',
    # 'description': """
    #Description text
    # """,
    # data files always loaded at installation
    # data files containing optionally loaded demonstration data
    #'demo': [
    #   'demo/demo_data.xml',
    #],
}