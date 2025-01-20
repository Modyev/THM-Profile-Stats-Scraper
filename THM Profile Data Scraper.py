import requests
import json
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

#response = requests.get("https://tryhackme.com/api/v2/public-profile/completed-rooms?user=672c63a02b416d46cd836b4f&limit=16&page=1")

username = input(f"Whats your {Fore.RED}TryHackMe{Fore.WHITE}.com{Style.RESET_ALL} Username?: {Fore.LIGHTWHITE_EX}")



response = requests.get("https://tryhackme.com/api/v2/public-profile?username=" + username)
_json = json.loads(response.text)

if _json["status"] == "error":
    print("Error Occured: " + _json["message"])
    exit()

data = _json["data"]

level = data["level"]
country = data["country"]
badgeCount = data["badgesNumber"]
roomsCount = data["completedRoomsNumber"]
rank = data["rank"]
rankPercentage = data["topPercentage"]

subscribed = None
if data["subscribed"] == 1:
    subscribed = True
else:
    subscribed = False
    
print(f"\n{Style.RESET_ALL}Hello there {Fore.GREEN}{username}{Style.RESET_ALL}!")

print(f"\nHere are your {Fore.RED}THM { Style.RESET_ALL}Profile Details: \n")
print(f"You are ranked the {Fore.BLUE}{rank}{Fore.LIGHTBLACK_EX}th{Style.RESET_ALL} on the platform!")
print(f"You are among the top {Fore.LIGHTBLUE_EX}{rankPercentage}{Fore.LIGHTBLACK_EX}%{Style.RESET_ALL} Users on the platform")
print(f"Your level is: {Fore.GREEN}{level}{Style.RESET_ALL}")
print(f"Your country is: {Fore.CYAN}{country}{Style.RESET_ALL}")
print(f"You have completed {Fore.YELLOW}{roomsCount}{Style.RESET_ALL} Rooms!")
print(f"You have {Fore.LIGHTMAGENTA_EX}{badgeCount}{Style.RESET_ALL} Badges!")

if subscribed:
    print(f"You are {Fore.YELLOW}subscribed{Style.RESET_ALL} to {Fore.WHITE}Premium{Style.RESET_ALL}!")
else:
    print(f"You are {Fore.RED}NOT{Style.RESET_ALL} subscribed to Premium!")

input()
