import asyncio
import requests
from colorama import init, Fore

print(Fore.LIGHTCYAN_EX + '''
 ▄▀▀█▄▄   ▄▀▀▀▀▄  ▄▀▄▄▄▄       ▄▀▀▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀▄ ▄▀▄  ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄ 
█ ▄▀   █ █ █   ▐ █ █    ▌     █ █   ▐ █   █   █ ▐ ▄▀ ▀▄ █  █ ▀  █ █  █ ▀  █ ▐  ▄▀   ▐ █   █   █ 
▐ █    █    ▀▄   ▐ █             ▀▄   ▐  █▀▀▀▀    █▄▄▄█ ▐  █    █ ▐  █    █   █▄▄▄▄▄  ▐  █▀▀█▀  
  █    █ ▀▄   █    █          ▀▄   █     █       ▄▀   █   █    █    █    █    █    ▌   ▄▀    █  
 ▄▀▄▄▄▄▀  █▀▀▀    ▄▀▄▄▄▄▀      █▀▀▀    ▄▀       █   ▄▀  ▄▀   ▄▀   ▄▀   ▄▀    ▄▀▄▄▄▄   █     █   
█     ▐   ▐      █     ▐       ▐      █         ▐   ▐   █    █    █    █     █    ▐   ▐     ▐   
▐                ▐                    ▐                 ▐    ▐    ▐    ▐     ▐                  ''')

async def send_message(webhook_url, message):
    payload = {
        'content': message
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print(Fore.GREEN + "spammed")
    else:
        print(Fore.GREEN + "error")

async def main():
    webhook_url = input(Fore.LIGHTGREEN_EX +"webhook url: ")
    message = input(Fore.LIGHTGREEN_EX +"message: ")
    message_count = int(input("number of messages: "))

    for i in range(message_count):
        await send_message(webhook_url, message)
        await asyncio.sleep(0)

asyncio.run(main())