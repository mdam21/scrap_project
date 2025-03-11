SITE_CONFIG = {
    "CNN": {
        "title_selector": "h1.article-title",
        "content_selector": "div.article-content",
        "max_retries": 5
    },
    "BBC": {
        "title_selector": "h1.story-headline",
        "content_selector": "div.story-body",
        "dynamic_load": True  # Ej: Requiere scroll
    },
    "el_universo": {
        "title_selector": "h1",
        "content_selector": "div.field-items",
        "dynamic_load": False
    }
}