
def code_interface(ctx) -> dict:
    list_code = iter(ctx)
    data_interface = {}

    for item in list_code:
        data_interface[item[0]] = {
            "id" : item[0],
            "id_category" : item[1],
            "url" : item[2],
            "title" : item[3],
            "syntax" : item[4],
            "description" : item[5],
            "created_at" : item[6],
            "updated_at" : item[7],
            "deleted_at" : item[8]
        }
    return data_interface

def category_interface(ctx) -> dict:
    list_category = iter(ctx)
    data_interface = {}

    for item in list_category:
        data_interface[item[0]] = {
            "id" : item[0],
            "category" : item[1],
            "description" : item[2]
        }
    return data_interface
