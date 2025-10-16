# Chrome Extension Remover (Node.js)

A simple Node.js tool to remove unauthorized Chrome extensions from Windows devices.

## How It Works

- Scans the local Chrome extensions folder.
- Removes all extensions not listed in the `WHITELIST` variable in the script.

## Usage

1. **Edit the whitelist:**  
   Open `chrome-extension-remover.js` and add the extension IDs you want to allow to the `WHITELIST` list.

2. **Install dependencies:**  
   No dependencies required (uses built-in Node.js modules).

3. **Run the script:**  
   ```sh
   node chrome-extension-remover.js
   ```
   Or, if installed as an npm package globally:
   ```sh
   npx chrome-extension-remover
   ```
   Or, if installed globally:
   ```sh
   chrome-extension-remover
   ```

## Notes

- Only works on Windows (`AppData` path).
- Run with a user account that has access to Chrome's extension directory.

## License

MIT
