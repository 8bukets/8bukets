import urllib.robotparser
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def check_permissions(url, user_agent):
    rp = urllib.robotparser.RobotFileParser()
    robots_url = f"{url}/robots.txt"
    logging.info(f"Checking robots.txt at {robots_url} for agent '{user_agent}'...")

    try:
        rp.set_url(robots_url)
        rp.read()

        can_fetch = rp.can_fetch(user_agent, "/")
        logging.info(f"Can '{user_agent}' fetch '/'? {'YES' if can_fetch else 'NO'}")

        # Check a disallowed path if any (in our case mostly allowed, but let's check basic root)
        return can_fetch
    except Exception as e:
        logging.error(f"Error checking robots.txt: {e}")
        return False

if __name__ == "__main__":
    base_url = "http://localhost:8000"

    # Test with Googlebot
    check_permissions(base_url, "Googlebot")

    # Test with a made-up bad bot (defaults to * rule)
    check_permissions(base_url, "BadBot")
