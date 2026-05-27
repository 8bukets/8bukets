import requests
import json
import os
import re

def get_next_page_url(link_header):
    if not link_header:
        return None

    # Parse the Link header to find the 'next' URL
    links = link_header.split(',')
    for link in links:
        match = re.match(r'<(.*?)>; rel="next"', link.strip())
        if match:
            return match.group(1)
    return None

def scrape_opentelemetry_repos():
    org_name = "open-telemetry"
    base_url = f"https://api.github.com/orgs/{org_name}/repos?per_page=100"

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "python-requests/opentelemetry-scraper"
    }

    print(f"Fetching repositories for GitHub organization: {org_name}...")

    all_repos = []
    url = base_url

    while url:
        print(f"Fetching {url}...")
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            repos = response.json()
            all_repos.extend(repos)

            # Check for pagination
            link_header = response.headers.get('Link')
            url = get_next_page_url(link_header)

        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            break

    print(f"Successfully fetched a total of {len(all_repos)} repositories.")

    # Process and clean the data
    processed_repos = []
    for repo in all_repos:
        repo_data = {
            "name": repo.get("name"),
            "full_name": repo.get("full_name"),
            "description": repo.get("description"),
            "html_url": repo.get("html_url"),
            "language": repo.get("language"),
            "stargazers_count": repo.get("stargazers_count"),
            "forks_count": repo.get("forks_count"),
            "archived": repo.get("archived"),
            "created_at": repo.get("created_at"),
            "updated_at": repo.get("updated_at")
        }
        processed_repos.append(repo_data)

    # Sort repos by stars descending
    processed_repos.sort(key=lambda x: x.get("stargazers_count", 0), reverse=True)

    # Save to JSON
    json_path = "opentelemetry_repos.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(processed_repos, f, indent=4, ensure_ascii=False)
    print(f"Saved JSON data to {json_path}")

    # Save to Markdown
    md_path = "opentelemetry_repos.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# OpenTelemetry GitHub Repositories\n\n")
        f.write(f"Scraped from [https://github.com/open-telemetry](https://github.com/open-telemetry)\n\n")
        f.write(f"Total repositories: {len(processed_repos)}\n\n")

        for repo in processed_repos:
            archived_badge = " **(ARCHIVED)**" if repo.get("archived") else ""
            f.write(f"## [{repo['name']}]({repo['html_url']}){archived_badge}\n\n")

            desc = repo['description'] if repo['description'] else "No description provided."
            f.write(f"{desc}\n\n")

            # Use standard defaults if values are missing
            lang = repo['language'] if repo['language'] else "N/A"
            stars = repo['stargazers_count'] if repo['stargazers_count'] is not None else 0
            forks = repo['forks_count'] if repo['forks_count'] is not None else 0

            f.write(f"- **Language:** {lang}\n")
            f.write(f"- **Stars:** {stars}\n")
            f.write(f"- **Forks:** {forks}\n\n")

        f.write("\n---\nAll the best - https://markposition.wordpress.com\n")

    print(f"Saved Markdown data to {md_path}")

if __name__ == "__main__":
    scrape_opentelemetry_repos()
