import os
import eel
from colorama import *

os.system("")
print("app")

@eel.expose
def refresh():
    print(f"{Fore.GREEN}Python is ready...{Fore.RESET}")

eel.init("www")
eel.start("index.html", size=(746, 683))