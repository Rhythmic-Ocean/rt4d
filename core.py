import requests
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv

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
        print(f"{username}'s current PP: {pp}")
    else:
        print("Failed to get user data. Response:", response.text)

def main():
    token = get_access_token()
    num = int(input("Add new user? (type 1) OR Get latest pp for all existing users (type 2): "))

    master = ["OnlyHadley", "EthantrixV3"]
    ranker = ["zNublao"]
    elite = ["rockhard", "Floofies", "bowiepro"]
    diamond = ["Wutever", "DZHEYLO", "nunk7", "zacfr", "InkLyned", "Am1x"]
    platinum = ["Saiba","plus","oppanboy","Arirret","Yumirai","Demideum","FinBois","zeppelinn","LevelOzone","durante","[Kanna]"]
    gold = ["rzye", "EonDuoLatios", "6 digit forever", "Daribush", "Egorixxz", "spinneracc", "thatanimeguy0", "ShoeSpoon", "Elo4373", "glowstickles", "golem", "Stagz", "wetratz0", "Death9208"]
    silver = ["Rika Voort", "shira1", "castor", "xXKero", "Strivial", "SqueakSqueak", "Rhythmic_Ocean", "KanekiKenLol", "alonsz", "SupNeit", "Kqma", "jefferson bobbe", "Amamiya Mitoro", "Xapped"]
    bronze = ["Slowpoke1360", "Solar_Taichi", "NotPole"]

    if num == 1:
        running = True
        while running:
            num1 = int(input("rank?: master(1), ranker(2), elite(3), diamond(4), platinum(5), gold(6), silver(7), bronze(8). Please type the corresponding number:"))
            new_name = input("Enter the name: ")
            if num1 == 1:
                master.append(new_name)

            elif num1 == 2:
                ranker.append(new_name)

            elif num1 == 3:
                elite.append(new_name)
        
            elif num1 == 4:
                diamond.append(new_name)

            elif num1 == 5:
                platinum.append(new_name)

            elif num1 == 6:
                gold.append(new_name)


            elif num1 == 7:
                silver.append(new_name)

        
            elif num1 == 8:
                bronze.append(new_name)
            

            num2 = int(input("Do you want to continue? 1-> yes, 2-> no"))
            if num2 == 2:
                running = False
        
    if token:
        print("Master\n")
        for user in master:
            get_user_pp(user, token)
        print("\n\n")

        print("Ranker\n")
        for user in ranker:
            get_user_pp(user, token)
        print("\n\n")

        print("Elite\n")
        for user in elite:
            get_user_pp(user, token)
        print("\n\n")

        print("Diamond\n")
        for user in diamond:
            get_user_pp(user, token)
        print("\n\n")

        print("Platinum\n")
        for user in platinum:
            get_user_pp(user, token)
        print("\n\n")

        print("Gold\n")
        for user in gold:
            get_user_pp(user, token)
        print("\n\n")

        print("Silver\n")
        for user in silver:
            get_user_pp(user, token)
        print("\n\n")

        print("Bronze\n")
        for user in bronze:
            get_user_pp(user, token)
 
        
         

if __name__ == "__main__":
    main()
