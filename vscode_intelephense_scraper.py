import requests
import json
import base64
import logging

logger = logging.getLogger("VSCodeIntelephenseScraper")

def scrape_vscode_intelephense():
    repo_url = "https://api.github.com/repos/bmewburn/vscode-intelephense"
    readme_url = "https://api.github.com/repos/bmewburn/vscode-intelephense/readme"

    logger.info(f"Fetching repository metadata from {repo_url}...")

    try:
        # Fetch Repo Metadata
        repo_resp = requests.get(repo_url, timeout=10)
        repo_resp.raise_for_status()
        repo_data = repo_resp.json()

        # Fetch README
        logger.info(f"Fetching repository README from {readme_url}...")
        readme_resp = requests.get(readme_url, timeout=10)
        readme_resp.raise_for_status()
        readme_json = readme_resp.json()

        # Decode README content (base64)
        readme_content = base64.b64decode(readme_json.get("content", "")).decode("utf-8")

        # Structure the data
        data = {
            "repository": {
                "name": repo_data.get("name"),
                "full_name": repo_data.get("full_name"),
                "description": repo_data.get("description"),
                "html_url": repo_data.get("html_url"),
                "stars": repo_data.get("stargazers_count"),
                "forks": repo_data.get("forks_count"),
                "language": repo_data.get("language"),
                "license": repo_data.get("license", {}).get("name") if repo_data.get("license") else None,
            },
            "readme": readme_content
        }

        # Save to JSON
        json_path = "vscode_intelephense_docs.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        logger.info(f"Saved VSCode Intelephense data to {json_path}")

        # Save to Markdown
        md_path = "vscode_intelephense_docs.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# {data['repository']['name']}\n\n")
            f.write(f"**Full Name:** {data['repository']['full_name']}\n\n")
            f.write(f"**Description:** {data['repository']['description']}\n\n")
            f.write(f"**URL:** {data['repository']['html_url']}\n\n")
            f.write(f"**Stars:** {data['repository']['stars']} | **Forks:** {data['repository']['forks']} | **Language:** {data['repository']['language']}\n\n")
            f.write(f"**License:** {data['repository']['license']}\n\n")
            f.write(f"---\n\n")
            f.write(f"## README\n\n")
            f.write(data["readme"])
            f.write("\n\n---\nAll the best - https://markposition.wordpress.com\n")

        logger.info(f"Saved VSCode Intelephense data to {md_path}")
        return True

    except requests.RequestException as e:
        logger.error(f"Error fetching data from GitHub API: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    scrape_vscode_intelephense()