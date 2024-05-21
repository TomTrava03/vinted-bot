# vinted-bot

HOW TO USE: for NOW(May 2024) the only way to make the bot work is by downloading the "main.py" file and have ALL the needed libraries installed with PIP.

resquester.py changes: // depending on the user location ex.it=italy

    "Host": "www.vinted.it" 
    self.VINTED_AUTH_URL = f"https://www.vinted.it/auth/token_refresh"
    Uncommented self.setCookies()

settings.py changes: // depending on the user location ex.it=italy

    VINTED_API_URL = f"https://www.vinted.it/api/v2
    
Remember to change the .it to wherever you're located. (ex. italy = .it, france = .fr)

HOW To RUN BOT:
1. Create a Discord Webhook and copy->write the url in an .env file as "URL=..."
2. Create a URL(Vinted) with appropriate filters for items you want to search
3. Run main.py -> C:/dir/to/main.py python3 URL(Vinted)

HOW THE BOT WORKS:
The bot takes the URL(Vinted) and uses it to search for the 10 newest items that fits the filters, than proceeds to send those items as Discord Webhook's messages.
This happens every 5 minutes without repeating already searched items. Remember to restart the bot every now and then to make sure the already seen items don't become 
too many for the computer to handle.
