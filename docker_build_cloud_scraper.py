import json
import logging
import os

logger = logging.getLogger("DockerBuildCloudScraper")

def load_docker_build_cloud_knowledge():
    """
    Since the knowledge was provided directly by the user, this 'scraper'
    simply validates the presence of the files and logs their loading
    to follow the system pattern of ensuring data is available for run_system.py.
    """
    logger.info("Loading Docker Build Cloud knowledge...")

    json_path = "docker_build_cloud_docs.json"
    md_path = "docker_build_cloud_docs.md"

    if not os.path.exists(json_path) or not os.path.exists(md_path):
        logger.error(f"Missing Docker Build Cloud knowledge files. Expected {json_path} and {md_path}")
        return False

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        logger.info(f"Successfully verified Docker Build Cloud knowledge: {data.get('title', 'Unknown Title')}")
        return True
    except Exception as e:
        logger.error(f"Failed to load Docker Build Cloud knowledge files: {e}")
        return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    load_docker_build_cloud_knowledge()