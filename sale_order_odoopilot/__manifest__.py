{
    'name': 'Sale Order OdooPilot Field',
    'version': '19.0.1.0.0',
    'category': 'Sales',
    'summary': 'Adds OdooPilot field under Payment Terms in Sale Orders',
    'description': """
Sale Order OdooPilot Field
===========================
This module adds a custom field 'OdooPilot' to sale orders,
positioned directly under the Payment Terms field.

Features:
* Custom character field on sale.order model
* Positioned after payment_term_id
* Visible in form and list views
* Tracking enabled for chatter
    """,
    'author': 'THE ADIL',
    'website': 'https://www.yourcompany.com',
    'depends': ['sale'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}