#!/usr/bin/env python3
import os
import shutil
import hashlib
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

ICLOUD_DRIVE = Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/8bukets_backup"
SOURCE_DIR = Path(__file__).resolve().parent.parent

TARGETS = [
    "data",
    "results",
    "antigravity/.jules_memory.json"
]

def get_md5(file_path):
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except FileNotFoundError:
        return None

def sync_file(src_path, dest_path):
    if not src_path.exists():
        logging.warning(f"Source file not found: {src_path}")
        return

    dest_path.parent.mkdir(parents=True, exist_ok=True)

    src_hash = get_md5(src_path)
    dest_hash = get_md5(dest_path)

    if src_hash != dest_hash:
        shutil.copy2(src_path, dest_path)
        logging.info(f"Synced {src_path.name} to iCloud.")
    else:
        logging.debug(f"Skipped {src_path.name} (unchanged).")

def sync_directory(src_dir, dest_dir):
    if not src_dir.exists():
        logging.warning(f"Source directory not found: {src_dir}")
        return

    for item in src_dir.rglob('*'):
        if item.is_file():
            rel_path = item.relative_to(src_dir)
            target_path = dest_dir / rel_path
            sync_file(item, target_path)

def run_sync():
    logging.info("Starting iCloud Sync...")
    try:
        ICLOUD_DRIVE.mkdir(parents=True, exist_ok=True)
        
        for target in TARGETS:
            src_target = SOURCE_DIR / target
            dest_target = ICLOUD_DRIVE / target

            if src_target.is_file():
                sync_file(src_target, dest_target)
            elif src_target.is_dir():
                sync_directory(src_target, dest_target)
            else:
                logging.warning(f"Target {target} does not exist. Skipping.")
                
        logging.info("iCloud Sync Completed Successfully.")
    except Exception as e:
        logging.error(f"Failed to synchronize to iCloud: {e}")

if __name__ == "__main__":
    run_sync()
