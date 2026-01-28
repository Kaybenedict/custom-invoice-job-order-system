{
    'name': 'Custom Invoice Description',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Adds a custom description field to invoice lines',
    'description': 'This module adds an extra description field to the lines in customer invoices.',
    'author': 'Kayode Adetifa',
    'depends': ['account'],
    'data': [
        'views/invoice_views.xml',
        'views/job_order_views.xml',
        'data/job_order_sequence.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

