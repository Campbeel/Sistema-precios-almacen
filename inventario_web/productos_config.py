PRODUCTOS_CONFIG = {
    "codigo_barra": {
        "label": "Productos con codigo de barra",
        "table": "productos_codigo_barra",
        "code_field": "codigo_barra",
        "code_label": "Codigo de barra",
        "price_field": "precio",
        "price_label": "Precio",
        "has_quantity": True,
    },
    "sin_codigo": {
        "label": "Productos sin codigo de barra",
        "table": "productos_sin_codigo",
        "code_field": "codigo_interno",
        "code_label": "Codigo interno",
        "price_field": "precio",
        "price_label": "Precio",
        "has_quantity": True,
    },
    "granel": {
        "label": "Productos a granel",
        "table": "productos_granel",
        "code_field": "codigo_interno",
        "code_label": "Codigo interno",
        "price_field": "precio_kilo",
        "price_label": "Precio por kilo",
        "has_quantity": False,
    },
}

DEFAULT_PRODUCT_TYPE = "codigo_barra"
