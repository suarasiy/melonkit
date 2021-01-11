import sqlite3
from package.Interface import *

db_path = "../db/"
db_name = "melonkit.db"
db_source = f"{db_path}{db_name}"

def set_dbpath(path):
    global db_path
    global db_name
    global db_source
    
    db_path = path
    db_source = f"{db_path}{db_name}"

def on_foreign(cursor):
    cursor.execute("PRAGMA foreign_keys = ON")

def insert_categories(category, description):
    connection = sqlite3.connect(db_source)
    cursor = connection.cursor()

    query = """
            INSERT INTO category
            VALUES (NULL, ?, ?)
            """
    try:
        cursor.execute(query, (category, description))
    except sqlite3.OperationalError as ex:
        print(ex)
        return connection.close()

    connection.commit()
    connection.close()

def update_categories(id, category, description):
    connection = sqlite3.connect("db/db/melonkit.db")
    cursor = connection.cursor()

    query = """
            UPDATE category
            SET category = ?,
                description = ?
            WHERE id = ?
            """
    
    try:
        cursor.execute(query, (category, description, id))
    except sqlite3.OperationalError as ex:
        print(ex)
        return connection.close()

    connection.commit()
    connection.close()

def insert_code(id_categories, url, title, syntax, description):
    connection = sqlite3.connect(db_source)
    cursor = connection.cursor()
    on_foreign(cursor)

    query = """
            INSERT INTO code
            VALUES (
                NULL, ?, ?, ?, ?, ?, datetime("now", "localtime"), datetime("now", "localtime"), NULL
            )
            """
    try:
        cursor.execute(query, (id_categories, url, title, syntax, description))
    except sqlite3.IntegrityError as ex:
        print(ex)
        return connection.close()

    connection.commit()
    connection.close()

def update_code(id, id_categories, url, title, syntax, description):
    connection = sqlite3.connect(db_source)
    cursor = connection.cursor()
    on_foreign(cursor)

    query = """
            UPDATE code
            SET id_category = ?,
                url = ?,
                title = ?,
                syntax = ?,
                description = ?,
                updated_at = datetime("now", "localtime")
            WHERE id = ?
            """
    
    try:
        cursor.execute(query, (id_categories, url, title, syntax, description, id))
    except sqlite3.IntegrityError as ex:
        print(ex)
        return connection.close()

    connection.commit()
    connection.close()

def soft_delete_code(id):
    connection = sqlite3.connect(db_source)
    cursor = connection.cursor()

    query = """
            UPDATE code
            SET deleted_at = datetime("now", "localtime")
            WHERE id = ?
            """

    cursor.execute(query, (id,))
    
    connection.commit()
    connection.close()

def delete_code(id):
    connection = sqlite3.connect(db_source)
    cursor = connection.cursor()

    query = """
            DELETE FROM code
            WHERE id = ?
            """
    cursor.execute(query, (id,))

    connection.commit()
    connection.close()

def restore_code(_id: int = None, mode: str = "single"):
    if _id is None and mode.lower() == "single":
        return {"message" : "Parameter cannot be empty."}

    connection = sqlite3.connect(db_source)
    cursor = connection.cursor()

    if mode.lower() == "single":
        query = """
                UPDATE code
                SET deleted_at = NULL
                WHERE id = ?
                """
        cursor.execute(query, (_id,))

    elif mode.lower() == "all":
        query = """
                UPDATE code
                SET deleted_at = NULL
                """
        cursor.execute(query)

    connection.commit()
    connection.close()

def show_code(order: str = "DESC") -> dict:
    connection = sqlite3.connect(db_source)
    cursor = connection.cursor()

    query = f'''
            SELECT * FROM code
            WHERE deleted_at is NULL
            ORDER BY updated_at {order}
            '''
    
    context = cursor.execute(query)
    result = context.fetchall()

    result = code_interface(result)
    result

    connection.close()
    return result

def show_code_recycle(order: str = "DESC") -> list:
    connection = sqlite3.connect(db_source)
    cursor = connection.cursor()

    query = f"""
            SELECT * FROM code
            WHERE deleted_at IS NOT NULL
            ORDER BY deleted_at {order}
            """
    
    context = cursor.execute(query)
    result = context.fetchall()

    connection.close()
    return result

def find_code(_id: int = None, title: str = None) -> dict:
    if _id is None and title is None:
        return {"message" : "Parameter cannot be empty."}

    connection = sqlite3.connect(db_source)
    cursor = connection.cursor()

    result = None
    
    if _id and not title:
        query = """
                SELECT * FROM code
                WHERE id = ?
                """
        
        context = cursor.execute(query, (_id,))
        result = context.fetchone()
    
    elif title and not _id:
        query = f"""
                SELECT * FROM code
                WHERE title LIKE '%{title}%'
                """
        context = cursor.execute(query)
        result = context.fetchall()
    
    result = code_interface(result)

    connection.close()
    return result

def filter_code(lang) -> dict:
    if lang is None:
        return {"message" : "Lang is empty!"}
    
    connection = sqlite3.connect(db_source)
    cursor = connection.cursor()

    query = """
            SELECT * FROM code
            WHERE id_category = ?
            ORDER BY updated_at DESC
            """

    context = cursor.execute(query, (lang,))
    result = context.fetchall()

    result = code_interface(result)

    connection.close()
    return result

def show_categories(order: str = "ASC") -> list:
    connection = sqlite3.connect(db_source)
    cursor = connection.cursor()

    query = f'''
            SELECT * FROM category
            ORDER BY category {order}
            '''
    
    context = cursor.execute(query)
    result = context.fetchall()

    connection.close()
    return result

def find_categories(_id: int = None, category: str = None) -> list:
    if _id is None and category is None:
        return {"message" : "Parameter cannot be empty."}

    connection = sqlite3.connect(db_source)
    cursor = connection.cursor()

    result = None

    if _id and not category:
        query = """
                SELECT * FROM category
                WHERE id = ?
                """
        
        context = cursor.execute(query, (_id,))
        result = context.fetchone()
    
    elif category and not _id:
        query = f"""
                SELECT * FROM category
                WHERE category LIKE '{category}'
                """
        
        context = cursor.execute(query)
        result = context.fetchone()
    
    connection.close()
    return result
