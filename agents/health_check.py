from .base_agent import BaseAgent
import requests
import urllib.robotparser

class HealthCheckAgent(BaseAgent):
    def __init__(self):
        super().__init__("HealthCheck")

    def perform_task(self, data):
        url = "https://informaticmagazine.data.blog"
        status = {}

        # 1. Check Site Availability
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                status["site_status"] = "healthy"
                status["site_code"] = 200
            else:
                status["site_status"] = "unhealthy"
                status["site_code"] = response.status_code
        except Exception as e:
            status["site_status"] = "down"
            status["site_error"] = str(e)

        # 2. Check Robots.txt
        robots_url = f"{url}/robots.txt"
        try:
            rp = urllib.robotparser.RobotFileParser()
            rp.set_url(robots_url)
            rp.read()

            # Check permissions for Googlebot
            can_fetch = rp.can_fetch("Googlebot", "/")
            status["robots_txt_accessible"] = True
            status["googlebot_allowed"] = can_fetch
        except Exception as e:
            status["robots_txt_accessible"] = False
            status["robots_txt_error"] = str(e)

        return status
