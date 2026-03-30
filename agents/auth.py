import os
import logging
from functools import wraps

logger = logging.getLogger("AuthManager")

class AuthManager:
    @staticmethod
    def verify_token(token: str) -> bool:
        """Simple token verification against environment variable."""
        expected_token = os.environ.get("SYSTEM_AUTH_TOKEN", "default_dev_token")
        return token == expected_token

def require_auth(func):
    """Decorator to require authentication for system methods."""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        token = kwargs.get("auth_token") or (args[1] if len(args) > 1 and isinstance(args[1], str) else None)
        if not AuthManager.verify_token(token):
            logger.error("Authentication failed: Invalid or missing token.")
            raise PermissionError("Access Denied: Invalid Authentication Token.")
        return await func(*args, **kwargs)
    return wrapper
