## 2024-05-23 - SSRF Prevention in Scrapers
**Vulnerability:** Scrapers blindly following pagination links can be tricked into accessing internal networks (SSRF) if the target site is compromised or malicious.
**Learning:** Checking 'http/https' scheme is insufficient; explicit DNS resolution and IP validation against private/loopback ranges is required.
**Prevention:** Use `is_safe_url` helper that resolves DNS and checks `ipaddress.is_private` before making requests.
