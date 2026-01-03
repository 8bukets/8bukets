from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse
from agents.base_agent import BaseAgent

class RobotsAgent(BaseAgent):
    """Agent for respecting robots.txt protocols."""

    def __init__(self):
        super().__init__("RobotsAgent")
        self.parsers = {}

    def process(self, url: str) -> bool:
        """
        Checks if the URL is allowed by robots.txt.
        """
        self.log(f"Checking robots.txt for {url}...")
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

        if base_url not in self.parsers:
            parser = RobotFileParser()
            parser.set_url(f"{base_url}/robots.txt")
            try:
                parser.read()
                self.parsers[base_url] = parser
            except Exception as e: # pylint: disable=broad-exception-caught
                self.log(f"Failed to read robots.txt for {base_url}: {e}")
                # Fail open if robots.txt is unreachable
                return True

        return self.parsers[base_url].can_fetch("*", url)

class CookieJarAgent(BaseAgent):
    """Agent for managing shared cookie state/context."""

    def __init__(self):
        super().__init__("CookieJar")
        self.cookies = {}

    def process(self, context: dict) -> None:
        """
        Updates shared cookie state.
        """
        self.log("Updating shared cookie context...")
        self.cookies.update(context)

    def get_cookies(self):
        """Returns the current cookie jar."""
        return self.cookies
