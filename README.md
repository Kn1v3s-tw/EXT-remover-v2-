# Chrome Extension Remover

A simple Python tool to remove unauthorized Chrome extensions from Windows devices.

## How It Works

- Scans the local Chrome extensions folder.
- Removes all extensions not listed in the `WHITELIST` variable in the script.

## Usage

1. **Edit the whitelist:**  
   Open `chrome_extension_remover.py` and add the extension IDs you want to allow to the `WHITELIST` list.

2. **Run the script:**  
   ```sh
   python chrome_extension_remover.py
   ```
   - Requires Python 3.x.
   - Run in a Command Prompt or Terminal window.

## Notes

- Only works on Windows (`%LOCALAPPDATA%` path).
- Run with a user account that has access to Chrome's extension directory.

## License

MIT
