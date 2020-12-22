#create database melonkit

import sqlite3

conn = sqlite3.connect('melonkit.db')
c = conn.cursor()

print("Opened database successfully")

# create table
# c.execute('''CREATE TABLE CATAGORY
#             (id             INT PRIMARY KEY    NOT NULL,              
#             category        VARCHAR            NOT NULL,
#             description     VARCHAR            NOT NULL)''')

# c.execute('''CREATE TABLE CODE
#             (id             INT PRIMARY KEY    NOT NULL,
#             id_catagory     INT                NOT NULL,
#             url             VARCHAR            NOT NULL,
#             title           VARCHAR            NOT NULL,
#             systax          MEDIUMTEXT         NOT NULL,
#             description     VARCHAR            NOT NULL,
#             create_at       DATETIME           NOT NULL,
#             updated_at      DATETIME           DEFAULT(NULL),
#             deleted_at      DATETIME           DEFAULT(NULL),
#             FOREIGN KEY(id_catagory)REFERENCES CATEGORY(id))''')



def insertData(name_database,id,id_catagory,url,title,systax,description_code,catagory_language,description_language):
      if name_database == 'CODE':
            insert = "INSERT INTO CODE (id,id_catagory,url,title,systax,description,create_at) \
                      VALUES({},{},'{}','{}','''{}''','{}',CURRENT_TIMESTAMP) \
                      ".format(id,id_catagory,url,title,systax,description_code)
      elif name_database == 'CATEGORY':
            id_catagory = id    
            insert = "INSERT INTO CATEGORY (id,catagory,description) \
                      VALUES({},'{}','{}') \
                      ".format(id,catagory_language,description_language)
                   
      return c.execute(insert)

def updateData(name_database,index_change,value_change,id):
      update = "UPDATE '{}' set '{}' = '{}'  WHERE id = '{}'".format(name_database,index_change,value_change,id)
      update = "UPDATE '{}' set updated_at = CURRENT_TIMESTAMP WHERE id = '{}'".format(name_database,id)
      conn.commit()
      return c.execute(update)

def readData(name_database):
      read = "SELECT * from '{}'".format(name_database)
      c.execute(read)
      return print(c.fetchall())
      
def deleteData(name_database,id):
      delete = "DELETE from '{}' where ID = {}".format(name_database,id)
      delete = "UPDATE '{}' set deleted_at = CURRENT_TIMESTAMP WHERE id = '{}'".format(name_database,id)
      conn.commit()
      return c.execute(delete)



# url = 'https://stackoverflow.com/questions/5601931/what-is-the-best-and-safest-way-to-merge-a-git-branch-into-master'
# systax = r'''
# print("hello world")
# '''

# insertData("CODE",1,1,url,"membangun dengan python",systax,"mencoba python","python","python")
# conn.commit()

# readData("CODE")
# conn.close()