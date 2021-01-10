import os
import eel
from colorama import *
from Query import *
from datetime import datetime

os.system("")
print("app")

@eel.expose
def get_list():
    for item in show_code():
        categories = find_categories(item[1])[1]
        title = item[3]
        url = item[2]
        description = item[5]
        created_at = item[6]
        
        dateconv = datetime.strptime(created_at, r"%Y-%m-%d %H:%M:%S")
        clockconv = dateconv.strftime(r"%I:%M %p")
        dateconv = dateconv.strftime(r"%B %d, %Y")

        eel.code_list(
            categories.lower(), title, description, dateconv, clockconv, url
        )

@eel.expose
def refresh():
    print(f"{Fore.GREEN}Python is ready...{Fore.RESET}")

eel.init("www")
eel.start("index.html", size=(746, 683))