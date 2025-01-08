# my_custom_module/__manifest__.py
{
    "name": "Pfau Module",
    "version": "1.0.0",
    "author": "Pfau",
    "category": "Pfau/Pfau",
    "summary": "",
    "description": """""",
    "depends": ["base", "web", "sale", "purchase", "stock", "l10n_din5008"],
    "data": [
        "views/sale_views/inherit_sale_form_view.xml",
        "report/sale_quotation.xml",
        'views/sale_views/inherit_attribute_form_view.xml',
    ],
    "assets": {
        "web.report_assets_common": [
            "pfau/static/src/**/*",
        ],
    },
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    "auto_install": False,
}
