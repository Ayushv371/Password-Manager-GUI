# Password Manager

A simple yet efficient password manager built using Python and Tkinter. This application allows users to store and retrieve their credentials securely, generate strong passwords, and save them in a JSON file for later use.

## Features
- **Secure Password Storage**: Save credentials securely in a JSON file.
- **Password Generator**: Automatically generates strong and random passwords.
- **Clipboard Support**: Copies generated passwords to clipboard for easy pasting.
- **User-Friendly Interface**: Built using Tkinter for a simple and intuitive UI.

## Requirements
Ensure you have the following installed:
- Python 3.x
- `tkinter` (comes with Python by default)
- `pyperclip` (for clipboard functionality)

Install required dependencies using:
```sh
pip install pyperclip
```

## How to Use
1. Run the script:
   ```sh
   python password_manager.py
   ```
2. Enter the website, email/username, and password.
3. Click "Generate Password" to create a strong password.
4. Click "Add" to save the credentials securely.

## File Structure
- `password_manager.py` - The main script for the application.
- `data.json` - Stores saved credentials (created automatically upon first use).
- `pass_logo.png` - Logo used in the UI.

## Data Storage
All passwords and related information are stored in `data.json` in the following format:
```json
{
    "example.com": {
        "email": "user@example.com",
        "password": "securepassword123"
    }
}
```

## Security Considerations
- The passwords are stored in plain text within `data.json`, so make sure to keep the file secure.
- Consider encrypting the JSON file for added security.
- Do not share your `data.json` file publicly.
- 
