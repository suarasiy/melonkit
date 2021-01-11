import os
import eel
from colorama import *
from package.Query import *
from datetime import datetime

os.system("")
set_dbpath("db/")

@eel.expose
def get_list():
    eel.clear_code()
    context = show_code("DESC")
    context
    for key, item in context.items():
        categories = find_categories(item["id_category"])[1]
        title = item["title"]
        url = item["url"]
        description = item["description"]
        created_at = item["created_at"]
        
        dateconv = datetime.strptime(created_at, r"%Y-%m-%d %H:%M:%S")
        clockconv = dateconv.strftime(r"%I:%M %p")
        dateconv = dateconv.strftime(r"%B %d, %Y")

        eel.code_list(
            key, categories.lower(), title, description, dateconv, clockconv, url
        )

@eel.expose
def get_list_filter(lang):
    eel.clear_code()
    id_category = find_categories(category = lang)
    id_category
    if id_category is None:
        return {"message" : "Categories not found."}
    
    context = filter_code(id_category[0])
    context
    if context is None:
        return {"message" : "Code not found."}
    
    for key, item in context.items():
        categories = find_categories(item["id_category"])[1]
        title = item["title"]
        url = item["url"]
        description= item["description"]
        created_at = item["created_at"]

        dateconv = datetime.strptime(created_at, r"%Y-%m-%d %H:%M:%S")
        clockconv = dateconv.strftime(r"%I:%M %p")
        dateconv = dateconv.strftime(r"%B %d, %Y")

        eel.code_list(
            key, categories.lower(), title, description, dateconv, clockconv, url
        )

@eel.expose
def get_list_search(title):
    eel.clear_code()
    if title == "":
        title = " "
    context = find_code(title = title)
    title
    context
    for key, item in context.items():
        categories = find_categories(item["id_category"])[1]
        title = item["title"]
        url = item["url"]
        description = item["description"]
        created_at = item["created_at"]

        dateconv = datetime.strptime(created_at, r"%Y-%m-%d %H:%M:%S")
        clockconv = dateconv.strftime(r"%I:%M %p")
        dateconv = dateconv.strftime(r"%B %d, %Y")

        eel.code_list(
            key, categories.lower(), title, description, dateconv, clockconv, url
        )

@eel.expose
def refresh():
    print(f"{Fore.GREEN}Python is ready...{Fore.RESET}")

eel.init("www")
eel.start("index.html", size=(746, 683), port=5555)