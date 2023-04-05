#!/usr/bin/env python

from pyVinted import Vinted
import requests
from datetime import datetime
import time
import pytz
import threading

TOKEN = "6225315802:AAHFxCXsAix1DW9DBYx2rOA-8xekLHqkGh8"  # TODO: check bot name, image profile and description


class Filter:
    def __init__(self, brand_id, price_to, sizes, other):
        self.brand_id = brand_id
        self.price_to = price_to
        self.sizes = sizes  # TODO: DICTIONARY
        self.other = other

    def __str__(self):
        url = f"https://www.vinted.it/vetement?order=newest_first&price_to={self.price_to}&currency=EUR&brand_id[]={self.brand_id}"
        for size in self.sizes:
            url += f"&size_id[]={size}"
        url += self.other
        return url  # f"https://www.vinted.it/vetement?order=newest_first&price_to={url.price_to}&currency=EUR"


def sendMessage(clock, item, chat_id):
    message = f"ITEM: {item.title}\nPRICE: {item.price}€\nURL: {item.url}\n"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        logs = open("logs.txt", "a")
        response = requests.post(url, json={'chat_id': chat_id, 'text': message})
        log = f"LOG[{clock}]: " + response.text + "\n"
        logs.write(log)
    except Exception as e:
        print(f"ERROR on REQUEST[{clock}]: " + str(e))


def run(vinted, filter, chat_id):
    global last_item
    first_iteration = True
    while True:
        clock = datetime.now(pytz.timezone('Europe/Rome')).strftime("%d/%m/%Y %H:%M:%S")

        try:
            url = filter.__str__()
            print(f"SEARCHING FOR: {filter.brand_id} ")
            items_list = vinted.items.search(url, 1, 1)
            item = items_list[0]
            if first_iteration:
                print(f"FOUND ITEM[{clock}]: " + item.title + " " + item.price + "€")
                sendMessage(clock, item, chat_id)
                first_iteration = False
                last_item = item
            elif last_item.title != item.title:
                print(f"FOUND ITEM[{clock}]: " + item.title + " " + item.price + "€")
                sendMessage(clock, item, chat_id)
                last_item = item

        except Exception as e:
            print(f"ERROR on SEARCH[{clock}]: " + str(e))
        time.sleep(30)


def init():  # where to initialize variables
    print("Write your Telegram Chat-id here: ")
    chat_id = input()
    vinted = Vinted()

    filters = []
    # Vinted URL variables  # TODO: GUI for this variables
    price_to = 35
    brand_id = 38923  # GOLDEN GOOSE
    sizes = {57: 37, 58: 38, 59: 39, 60: 40, 61: 41, 62: 42, 63: 43,
             776: 38, 778: 39, 780: 40, 782: 41, 784: 42, 786: 43, 788: 44, 790: 45, 792: 46,
             794: 47, 1190: 48, 1191: 49
             }  # it's size_id: size ex. 57(size 37 for woman) 776(size 38 for man)
    filters.append(Filter(brand_id, price_to, sizes, ""))
    price_to = 40
    brand_id = 1281  # PINKO
    other = "&catalog[]=19"  # bags
    filters.append(Filter(brand_id, price_to, sizes, other))

    threading.Thread(target=run, args=(vinted, filters[0], chat_id)).start()
    threading.Thread(target=run, args=(vinted, filters[1], chat_id)).start()
    # run(vinted, Filter(brand_id, price_to, sizes, ""))


if __name__ == '__main__':
    init()
