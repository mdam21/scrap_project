from functools import wraps
from utils.logger import log_execution
from src.browser_manager import iniciar_navegador

class BaseScraper:
    def __init__(self, browser_manager: iniciar_navegador):
        self.browser = browser_manager

    @log_execution
    def _retry_on_failure(self, max_retries=3):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                for attempt in range(max_retries):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        if attempt == max_retries - 1:
                            raise
                        self.browser.reload()
                return None
            return wrapper
        return decorator