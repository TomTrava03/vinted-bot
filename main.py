import sys
import pytz

from discord import Webhook
import aiohttp
import asyncio

# EXAMPLE for vinted.it url: https://www.vinted.it/catalog?order=newest_first&price_to=60&currency=EUR&brand_id[]=1281&catalog[]=19

# GLOBAL VARIABLES #
vinted = Vinted()

def write_log(clock, message): # Log FILE
    try:     
        logs = open("logs.txt", "a")
        log = f"LOG[{clock}]: " + message
        logs.write(log)
    except Exception as e:
        print(f"ERROR on MODIFYING LOG file {clock}]: " + str(e))

async def send_to_discord(clock, message): # Discord WEBHOOK
    # message = f"ITEM: {item.title}\nPRICE: {item.price}€\nURL: {item.url}\n"
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url_discord, session=session)
        await webhook.send(message, username='vinted-bot')

def run(url):

    old_items = set()
    first_iteration = True

    while True:
        clock = datetime.now(pytz.timezone('Europe/Rome')).strftime("%d/%m/%Y %H:%M:%S")
        
        try:
            new_items = set(vinted.items.search(url, 10, 1))
        except requests.ConnectionError, e:
            print(f"Errore[{clock}]: "e)

        print(f"\nDebugging: {clock}")
        for element in new_items:
            print(element.title)

        tmp = new_items.difference(old_items) 
        old_items = new_items #

        for element in tmp:
            message = f"ITEM: {element.title}\nPRICE: {element.price}€\nURL: {element.url}\n"
            # print(message)
            asyncio.run(send_to_discord(clock, message))
            write_log(clock, message)
        
        time.sleep(300)

def init(): 
    run(sys.argv[1])

if __name__ == '__main__':
    init()
