# vinted-telegram-bot

HOW TO INSTALL: for NOW (April 2nd 2023) the only way to make the bot work is by downloading the "main.py" file and have a full virtual environment for Python files.
In the future I'll make an .exe version of the FULL working bot.

resquester.py changes: // depending on the user location ex.it=italy

    "Host": "www.vinted.it" 
    self.VINTED_AUTH_URL = f"https://www.vinted.it/auth/token_refresh"
    Uncommented self.setCookies()

settings.py changes: // depending on the user location ex.it=italy

    VINTED_API_URL = f"https://www.vinted.it/api/v2
    
Remember to change the .it to wherever you're located. (ex. italy = .it, france = .fr)
