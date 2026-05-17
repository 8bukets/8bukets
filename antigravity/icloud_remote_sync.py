import os
import sys
import argparse
from pyicloud import PyiCloudService
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

APPLE_ID = os.environ.get("APPLE_ID")
APPLE_PASSWORD = os.environ.get("APPLE_PASSWORD")

def get_icloud_api():
    if not APPLE_ID or not APPLE_PASSWORD:
        print("⚠️ [iCloud-Remote] APPLE_ID and APPLE_PASSWORD not set. Remote sync unavailable.")
        return None

    print(f"🔄 [iCloud-Remote] Authenticating for {APPLE_ID}...")
    try:
        api = PyiCloudService(APPLE_ID, APPLE_PASSWORD)

        if api.requires_2fa:
            # Note: In a fully autonomous background task, this might fail unless a session is already trusted.
            print("⚠️ [iCloud-Remote] 2FA required. Manual intervention needed for first-time setup.")
            return None

        return api
    except Exception as e:
        print(f"❌ [iCloud-Remote] Authentication failed: {e}")
        return None

def sync_docker_files(api):
    if not api:
        return False

    target_folder_name = "antigravity-docker-sync"

    if target_folder_name not in api.drive.dir():
        print(f"📂 [iCloud-Remote] Creating folder '{target_folder_name}'...")
        try:
            api.drive.mkdir(target_folder_name)
        except:
            pass

    drive_folder = api.drive[target_folder_name]

    docker_files = [
        'Dockerfile',
        'docker-compose.yml',
        'docker-compose.cloud.yml',
        '.dockerignore',
        'autonomous_state.json' # Including system state as requested
    ]

    success_count = 0
    for filename in docker_files:
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                print(f"📤 [iCloud-Remote] Uploading {filename}...")
                try:
                    drive_folder.upload(f, name=filename)
                    success_count += 1
                except Exception as e:
                    print(f"❌ [iCloud-Remote] Failed to upload {filename}: {e}")

    print(f"✅ [iCloud-Remote] Remote sync complete. {success_count} files uploaded.")
    return True

if __name__ == "__main__":
    api = get_icloud_api()
    if api:
        if sync_docker_files(api):
            sys.exit(0)
        else:
            sys.exit(1)
    else:
        print("⏩ [iCloud-Remote] Skipping remote sync due to missing credentials or 2FA.")
        sys.exit(2) # Specific exit code for skip
