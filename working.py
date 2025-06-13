 
import gspread
from google.oauth2.service_account import Credentials
from core import get_pp

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]
creds = Credentials.from_service_account_file("credentials.json", scopes = scopes)
client = gspread.authorize(creds)
sheet_id = "1ltgGn8a-dXVsAbgbjwgQEKn83ow2houytfT79g5qUX4"
workbook = client.open_by_key(sheet_id)

def add_new_user():
    running = True
    while running:

        new_name = input("Enter the name: ")
        new_pp = get_pp(new_name)
        print(f"{new_name} has pp: {new_pp}\n")
        print("Which sheet? \n")
        num1 = int(input("rank?: master(8), ranker(7), elite(6), diamond(5), platinum(4), gold(3), silver(2), bronze(1). Please type the corresponding number:"))
        if not (1 <= num1 <= 8):
            print("Error: Invalid range")
            return
        sheet = workbook.get_worksheet(num1 - 1)
        col_a_values = sheet.col_values(1)
        next_row = len(col_a_values) + 1
        sheet.update(f"A{next_row}", [[new_name]])

        print("\n Username successfully added, would you like to add the user's current pp as OG pp?\n")
        num2 = int(input("1 -> yes, 2-> no\n"))
        if num2 == 1:
            sheet.update(f"G{next_row}", [[new_pp]])

        num2 = int(input("Do you want to continue? 1-> yes, 2-> no"))
        if num2 == 2:
            running = False


def main():
    running = True
    while running:
        ans1 = input("Click 1 if you would like to add a new User\n" 
                        "Click 2 if you would like to log OG pp\n" \
                        "Click 3 if you would want to log the pp change\n"
                        "Click 4 to safely exit: ")
        try:
            choice = int(ans1)
        except ValueError:
            print("Please enter a num (1-4)")
            continue
        if choice == 1:
            add_new_user()
        elif choice == 4:
            break
        else:
            continue

if __name__ == "__main__":
    main()

        
    


