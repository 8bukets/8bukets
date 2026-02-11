import json
import logging
import argparse
import os
import sys
from googlesearch import search
from typing import List, Dict

def validate_output_path(file_path: str):
    """
    Validates the output file path to prevent path traversal and overwriting sensitive files.
    Enforces that the file is written to the current working directory and has a safe extension.
    """
    # 1. Prevent Path Traversal
    abs_path = os.path.abspath(file_path)
    cwd = os.getcwd()

    # Use commonpath to check if the file is inside the CWD
    try:
        if os.path.commonpath([cwd, abs_path]) != cwd:
            raise ValueError("Output file must be within the current working directory.")
    except ValueError:
         raise ValueError("Output file must be within the current working directory.")

    # 2. Validate Extension
    allowed_extensions = ['.json']
    if not any(file_path.endswith(ext) for ext in allowed_extensions):
        raise ValueError(f"Invalid file extension. Allowed: {', '.join(allowed_extensions)}")

def configure_logging(verbose: bool):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def perform_google_search(query: str, num_results: int = 10, lang: str = "en") -> List[Dict[str, str]]:
    """
    Performs a Google search and returns a list of results.
    """
    logging.info(f"Searching Google for: '{query}' (limit: {num_results})")
    results = []

    try:
        search_results = search(query, num_results=num_results, lang=lang, advanced=True)

        for result in search_results:
            results.append({
                "title": result.title,
                "url": result.url,
                "description": result.description
            })

    except Exception as e:
        logging.error(f"Error during Google search: {e}")

    logging.info(f"Found {len(results)} results.")
    return results

def main():
    parser = argparse.ArgumentParser(description="Google Search Scraper")
    parser.add_argument("query", nargs="?", default="site:informaticmagazine.data.blog", help="Search query")
    parser.add_argument("-o", "--output", default="google_search_results.json", help="Output JSON file path")
    parser.add_argument("-n", "--limit", type=int, default=10, help="Number of results to retrieve (page one approx 10)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")

    args = parser.parse_args()

    configure_logging(args.verbose)

    try:
        validate_output_path(args.output)
    except ValueError as e:
        logging.error(f"Security Error: {e}")
        sys.exit(1)

    results = perform_google_search(args.query, num_results=args.limit)

    try:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
        logging.info(f"Saved results to {args.output}")
    except IOError as e:
        logging.error(f"Failed to save output to {args.output}: {e}")

if __name__ == "__main__":
    main()
