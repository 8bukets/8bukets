import json
import logging

class CookieJar:
    """
    A shared memory structure simulating a browser's cookie jar or
    server-side shared session state. Allows agents to leave 'cookies'
    (small pieces of data) for other agents or 3rd parties (simulated).
    """
    def __init__(self):
        self.cookies = {} # domain -> {name: value}
        self.logger = logging.getLogger("CookieJar")

    def set_cookie(self, domain, name, value, party="1st"):
        """
        Set a cookie.
        party: '1st' (internal), '2nd' (partner), '3rd' (external/tracking)
        """
        if domain not in self.cookies:
            self.cookies[domain] = {}

        self.cookies[domain][name] = {
            "value": value,
            "party": party,
            "created_at": "now" # In real app use datetime
        }
        self.logger.info(f"Cookie set: [{party}] {domain} -> {name}={value}")

    def get_cookie(self, domain, name):
        return self.cookies.get(domain, {}).get(name, {}).get("value")

    def get_cookies_for_domain(self, domain):
        return self.cookies.get(domain, {})

    def get_all_cookies(self):
        return self.cookies

    def dump(self):
        return json.dumps(self.cookies, indent=2)
