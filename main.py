from time import sleep
import requests
from threading import Thread

nombre = 0

def mute(token,id):
    global nombre
    a = requests.patch(f"https://discord.com/api/v9/users/@me/guilds/{id}/settings",json={"message_notifications":1},headers={"authorization":token})
    nombre += 1
    print(f"{nombre} servers was muted")

def main():
    a = input("Y/n Do you want to change all notif in only at ping\n\n >").lower()
    if a == "y":
        try:
            token = input("Your discord token\n\n >")
            getlist = requests.get("https://discord.com/api/v9/users/@me/guilds?limit=200",headers={"authorization":token}).json()
            for i in getlist :
              Thread(target=mute, args=(token,i["id"])).start()
        except Exception as e:
            print("An error occured ,Please check if you have a good token, the program restarting...")
            sleep(2)
            return main()
    elif a == "n":
        pass
    else:
        print("An error occured , the program restarting...")
        sleep(2)
        return main()


main()
