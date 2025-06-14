rt4d
To run the code on a Windows machine:

Step 1: Check if Python is installed
python --version

If Python is not recognized, install Python from https://python.org/downloads/
Make sure to check "Add Python to PATH" during installation.

Step 2: Create and activate a virtual environment (recommended)
python -m venv myenv
myenv\Scripts\activate

Step 3: Upgrade pip (optional but recommended)
python -m pip install --upgrade pip

Step 4: Install required packages
pip install gspread google-auth requests python-dotenv

Step 5: Place the following files in the same folder:
- working.py (your main script)
- core.py (your helper module)
- sec.env (environment variables file with AUTH_ID and AUTH_TOKEN)

Step 6: Get credentials from Google Console and osu! profile
- Go to your osu! profile settings, get your AUTH_ID and AUTH_TOKEN.
- Put them in the relevant blanks inside the file named sec.env.
- Go to Google Cloud Console, create a new project, enable Google Sheets API,
  and download the credentials file.
- Put the credentials file in the same folder and rename it to credentials.json.

Step 7: Grant permission on the Google Spreadsheet
- Find the service account email in credentials.json.
- Share your Google Spreadsheet with this email.
- Give it EDITOR permission to allow data manipulation.

Step 8: Run the program
python working.py

