#!/usr/bin/env python

from pyVinted import Vinted # modify Vinted library for .it site
from datetime import datetime
import time
import sys
import pytz

from discord import Webhook
import aiohttp
import asyncio
from dotenv import load_dotenv


# GLOBAL VARIABLES #
vinted = Vinted()

def write_log(clock, message): # Log FILE

    try:     
        logs = open("logs.txt", "a")
        log = f"LOG[{clock}]: " + message
        logs.write(log)
    except Exception as e:
        print(f"ERROR on MODIFYING LOG file {clock}]: " + str(e))

async def send_to_discord(clock, message, url_discord_webhook): # Discord WEBHOOK
    # message = f"ITEM: {item.title}\nPRICE: {item.price}€\nURL: {item.url}\n"
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url_discord_webhook, session=session)
        await webhook.send(message, username='vinted-bot')

def run(url_vinted, url_discord):

    old_items = set()
    first_iteration = True

    while True:
        clock = datetime.now(pytz.timezone('Europe/Rome')).strftime("%d/%m/%Y %H:%M:%S")
        
        try:
            new_items = set(vinted.items.search(url_vinted, 10, 1))
        except requests.ConnectionError, e:
            print(f"Errore[{clock}]: "e)

        print(f"\nDebugging: {clock}")
        for element in new_items:
            print(element.title)

        tmp = new_items.difference(old_items) 
        old_items = new_items 

        for element in tmp:
            message = f"ITEM: {element.title}\nPRICE: {element.price}€\nURL: {element.url}\n"
            asyncio.run(send_to_discord(clock, message, url_discord))
            write_log(clock, message)
        
        time.sleep(300)

def init(): 
    load_dotenv()
    run(sys.argv[1], os.getenv('URL'))
    

if __name__ == '__main__':
    init()
