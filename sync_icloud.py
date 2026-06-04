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
        print("Error: APPLE_ID and APPLE_PASSWORD must be set in .env file.")
        sys.exit(1)

    print(f"Authenticating to iCloud for {APPLE_ID}...")
    try:
        api = PyiCloudService(APPLE_ID, APPLE_PASSWORD)
    except Exception as e:
        print(f"Authentication failed: {e}")
        sys.exit(1)

    if api.requires_2fa:
        print("Two-factor authentication required.")
        code = input("Enter the code you received on one of your approved devices: ")
        result = api.validate_2fa_code(code)
        print("Code validation result:", result)

        if not result:
            print("Failed to verify security code")
            sys.exit(1)

        if not api.is_trusted_session:
            print("Session is not trusted. Requesting trust...")
            result = api.trust_session()
            print("Session trust result:", result)

            if not result:
                print("Failed to request trust. You will likely be prompted for the code again in the future")
    elif api.requires_2sa:
        import click
        print("Two-step authentication required. Your trusted devices are:")
        devices = api.trusted_devices
        for i, device in enumerate(devices):
            print(f"  {i}: {device.get('deviceName', 'SMS to {}'.format(device.get('phoneNumber')))}")

        device_index = int(click.prompt('Which device would you like to use?', default=0))
        device = devices[device_index]
        if not api.send_verification_code(device):
            print("Failed to send verification code")
            sys.exit(1)

        code = click.prompt('Please enter validation code')
        if not api.validate_verification_code(device, code):
            print("Failed to verify verification code")
            sys.exit(1)

    print("Successfully authenticated with iCloud!")
    return api


def ensure_icloud_folder(api, folder_name):
    # PyiCloud's drive API works nicely: api.drive['foldername']
    if folder_name not in api.drive.dir():
        print(f"Folder '{folder_name}' not found in iCloud Drive. Creating it...")
        try:
            api.drive.mkdir(folder_name)
        except Exception as e:
            print(f"Failed to create folder '{folder_name}' via pyicloud. Note: Folder creation might not be fully supported by the pyicloud API.")
            print(f"Error: {e}")
            print(f"Please create the folder '{folder_name}' manually in iCloud Drive first.")
            sys.exit(1)
    return api.drive[folder_name]


def upload_directory(icloud_folder, local_path):
    print(f"Uploading {local_path} to iCloud folder '{icloud_folder.name}'...")
    if not os.path.isdir(local_path):
        print(f"Local path '{local_path}' does not exist or is not a directory.")
        return

    # In iCloud, nested folders are tricky with pyicloud. We'll do a simple flat upload
    # or recreate structure if possible. For simplicity, we just use a basic recursive approach.
    for item in os.listdir(local_path):
        item_path = os.path.join(local_path, item)
        if os.path.isfile(item_path):
            with open(item_path, 'rb') as f:
                print(f"  Uploading file: {item_path}")
                try:
                    icloud_folder.upload(f, name=item)
                except Exception as e:
                    print(f"  Failed to upload {item_path}: {e}")
        elif os.path.isdir(item_path):
            if item in ['.git', '__pycache__', 'node_modules']:
                continue

            # Create subfolder in iCloud
            if item not in icloud_folder.dir():
                print(f"  Creating subfolder: {item}")
                try:
                    icloud_folder.mkdir(item)
                except Exception as e:
                    print(f"  Warning: Cannot create subfolder {item}: {e}")
                    continue

            upload_directory(icloud_folder[item], item_path)

def download_directory(icloud_folder, local_path):
    print(f"Downloading from iCloud folder '{icloud_folder.name}' to {local_path}...")
    if not os.path.exists(local_path):
        os.makedirs(local_path)

    for item_name in icloud_folder.dir():
        node = icloud_folder[item_name]
        item_path = os.path.join(local_path, item_name)

        if node.type == 'file':
            print(f"  Downloading file: {item_name}")
            try:
                with node.open(stream=True) as response:
                    with open(item_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
            except Exception as e:
                print(f"  Failed to download {item_name}: {e}")
        elif node.type == 'folder':
            if item_name in ['.git', '__pycache__', 'node_modules']:
                continue
            download_directory(node, item_path)


def main():
    parser = argparse.ArgumentParser(description="Sync files with iCloud Drive.")
    parser.add_argument("--upload", action="store_true", help="Upload local antigravity/ and .github/ folders to iCloud.")
    parser.add_argument("--pull", action="store_true", help="Pull files from iCloud into local antigravity/ and .github/ folders.")
    args = parser.parse_args()

    if not args.upload and not args.pull:
        print("Please specify either --upload or --pull.")
        parser.print_help()
        sys.exit(1)

    api = get_icloud_api()
    target_folder_name = "8bukets"
    icloud_target_folder = ensure_icloud_folder(api, target_folder_name)

    folders_to_sync = ['antigravity', '.github']

    if args.upload:
        for folder in folders_to_sync:
            if os.path.exists(folder):
                # Ensure a subfolder for each in 8bukets exists
                if folder not in icloud_target_folder.dir():
                    try:
                        icloud_target_folder.mkdir(folder)
                    except Exception as e:
                        print(f"Warning: Cannot create {folder} in iCloud: {e}. Please create it manually if upload fails.")

                # Check again if it exists after creation attempt
                if folder in icloud_target_folder.dir():
                    upload_directory(icloud_target_folder[folder], folder)
                else:
                    print(f"Skipping {folder} because target folder couldn't be created in iCloud.")
            else:
                print(f"Local folder {folder} not found, skipping.")

    if args.pull:
        for folder in folders_to_sync:
            if folder in icloud_target_folder.dir():
                download_directory(icloud_target_folder[folder], folder)
            else:
                print(f"Folder {folder} not found in iCloud {target_folder_name}, skipping.")

if __name__ == "__main__":
    main()
