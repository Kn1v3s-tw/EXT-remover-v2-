import os
import shutil

# Path to Chrome extensions (Windows)
CHROME_EXT_PATH = os.path.expandvars(
    r'%LOCALAPPDATA%\Google\Chrome\User Data\Default\Extensions'
)

# List of allowed extension IDs (whitelist)
WHITELIST = [
    'ehnniokiiebpinnfegpkdlcamgdcaaje',  # Example: Google Docs
    # Add more allowed extension IDs here
]

def remove_unwanted_extensions():
    if not os.path.exists(CHROME_EXT_PATH):
        print(f"Chrome extensions path does not exist: {CHROME_EXT_PATH}")
        return

    for ext_id in os.listdir(CHROME_EXT_PATH):
        if ext_id not in WHITELIST:
            ext_path = os.path.join(CHROME_EXT_PATH, ext_id)
            print(f"Removing extension: {ext_id}")
            shutil.rmtree(ext_path, ignore_errors=True)

if __name__ == "__main__":
    remove_unwanted_extensions()
    print("Extension cleanup complete.")