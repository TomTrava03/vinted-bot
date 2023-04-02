from pyVinted import Vinted
import requests
from datetime import datetime
import time
import pytz

TOKEN = "6225315802:AAHFxCXsAix1DW9DBYx2rOA-8xekLHqkGh8"
chat_ids = ["YOUR_TELEGRAM_CHAT_ID"]  # https://www.alphr.com/find-chat-id-telegram/


def run(vinted, order, price_to, currency, number_of_items, page):
    logs = open("logs.txt", "a")
    first_iteration = True
    while True:  # TODO: check if first item is different from before and then lower time.sleep()
        clock = datetime.now(pytz.timezone('Europe/Rome')).strftime("%d/%m/%Y %H:%M:%S")

        try:
            items_list = vinted.items.search(
                f"https://www.vinted.it/vetement?order={order}&price_to={price_to}&currency={currency}",
                number_of_items, page)  # TODO: da cambiare in caso altre variabili
            print(f"ITEM[{clock}]: "+items_list[0].title+" "+items_list[0].price+"€")
            current_item = items_list[0]
            if first_iteration:
                last_item = items_list[0]
            elif current_item != last_item:  # TODO: sistemare current_item and last_item
                last_item = current_item
                for chat_id in chat_ids:
                    message = f"OGGETTO: {items_list[0].title}\nPREZZO: {items_list[0].price}€\nURL: {items_list[0].url}"
                    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
                    try:
                        response = requests.post(url, json={'chat_id': chat_id, 'text': message})
                        log = f"LOG[{clock}]: " + response.text + "\n"
                        logs.write(log)
                    except Exception as e:
                        print(f"ERROR on REQUEST[{clock}]: " + str(e))
        except Exception as e:
            print(f"ERROR on SEARCH[{clock}]: " + str(e))
        time.sleep(30)


def init():  # where to initialize variables
    vinted = Vinted()

    order = "newest_first"  # Vinted URL variables  # TODO: GUI for this variables
    price_to = 60
    currency = "EUR"
    number_of_items = 1
    page = 1

    run(vinted, order, price_to, currency, number_of_items, page)


if __name__ == '__main__':
    init()
