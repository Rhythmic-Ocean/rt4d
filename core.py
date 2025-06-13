import requests
import sqlite3
from dotenv import load_dotenv
import os
import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]
creds = Credentials.from_service_account_file("credentials.json", scopes = scopes)
client = gspread.authorize(creds)
sheet_id = "1ltgGn8a-dXVsAbgbjwgQEKn83ow2houytfT79g5qUX4"
sheet = client.open_by_key(sheet_id)

values_list = sheet.sheet1.row_values(1)

load_dotenv(dotenv_path="sec.env")

CLIENT_ID = os.getenv("AUTH_ID")
CLIENT_SECRET = os.getenv("AUTH_TOKEN")

def get_access_token():
    url = 'https://osu.ppy.sh/oauth/token'
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials',
        'scope': 'public'
    }

    response = requests.post(url, json=data)

    if response.ok:
        return response.json()['access_token']
    else:
        print("Failed to get access token.")
        return None

def get_user_pp(username, token):
    url = f"https://osu.ppy.sh/api/v2/users/{username}/osu"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    if response.ok:
        data = response.json()
        pp = data['statistics']['pp']
        return pp
    else:
        print("Failed to get user data. Response:", response.text)
        return


def get_pp(user):
    token = get_access_token()
    if token:
            pp = get_user_pp(user, token)
            if pp:
                return pp
            else:
                return
    else:
        return
        
         

if __name__ == "__main__":
    main()
