# -*- coding: utf-8 -*-

{
    'name' : 'Account Budget Limit ',
    'author': "Secteur Networks for PGL",
    'version' : '12.0.1.2',
    'live_test_url':'https://youtu.be/Q-46v4WzE0M',
    "images":["static/description/main_screenshot.png"],
    'summary' : 'Accounting Budget Limit Alert Budget limit Warning against Purchase budget limit alerts against Bill budget exceed alerts budget limit alert accounting budget validation against purchase budget integration budget warning limit exceed warning on budget',
    'description' : """
        Allow Accounting Budget Limit Alert/Warning on  confirm Purchase Order and validate Vendor Bill
    """,
    "license" : "OPL-1",
    'depends' : ['base','purchase','account','stock', 'om_account_budget'],
    'data': [
            'security/ir.model.access.csv',
            'security/account_budget_security.xml',
            'views/account_budget_views.xml',
            'views/account_analytic_account_views.xml',
            'views/budget_view.xml',
            ],
    'qweb' : [],
    'demo' : [],
    'installable' : True,
    'auto_install' : False,
    'price': 58,
    'category' : 'Accounting',
    'currency': "EUR",
}
