{
    "name": "Noreflow – WhatsApp AI Assistant",
    "summary": "Connect Odoo to Noreflow: sales from Noreflow land in Odoo as invoices and payments, and an AI assistant answers your customers on WhatsApp in Arabic and English.",
    "version": "19.0.1.0.0",
    "category": "Accounting/Accounting",
    "author": "NOREFLOW LTD",
    "website": "https://noreflow.net",
    "license": "LGPL-3",
    "depends": ["account"],
    "data": [
        "security/ir.model.access.csv",
        "views/noreflow_connect_views.xml",
    ],
    "images": ["static/description/banner.png"],
    "installable": True,
    "application": False,
}
