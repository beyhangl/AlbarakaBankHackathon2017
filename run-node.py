import MySQLdb
import time
import chatterbotum as get_result
from chatterbot import ChatBot
import hazir_cumleler as banka_getir
import my_sql_operations as ancon
#from Naked.toolshed.shell import execute_js, muterun_js
from subprocess import call

# Note that you have to specify path to script
#call(["node", "path_to_script.js"])

def connection_mysql():
 db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="mysql",
                     db="albaraka")

 cursor = db.cursor()
 return cursor

def return_last_node_data_number():
 cursor=connection_mysql()
 cursor.execute("select max(id) from temp_node")
 numrows = cursor.rowcount
 for x in range(0, numrows):
     row = cursor.fetchone()
     my_id=row[0]
 return my_id


def return_last_data_number():
 cursor=connection_mysql()
 cursor.execute("select max(soruid) from chats")
 numrows = cursor.rowcount
 for x in range(0, numrows):
     row = cursor.fetchone()
     my_id=row[0]
 return my_id


def last_status():
 cursor=connection_mysql()
 cursor.execute("select status from chats where soruid=" + str(return_last_data_number()) )
 numrows = cursor.rowcount
 for x in range(0, numrows):
     row = cursor.fetchone()
     my_id=row[0]
 return my_id

def last_counter():
 cursor=connection_mysql()
 cursor.execute("select counter from chats where soruid=" + str(return_last_data_number()) )
 numrows = cursor.rowcount
 for x in range(0, numrows):
     row = cursor.fetchone()
     my_id=row[0]
 return my_id


def last_gelen_data():
 cursor=connection_mysql()
 cursor.execute("select gelen from chats where soruid=" + str(return_last_data_number()) )
 numrows = cursor.rowcount
 for x in range(0, numrows):
     row = cursor.fetchone()
     my_id=row[0]
 return my_id

def last_node_gelen_data():
 cursor=connection_mysql()
 cursor.execute("select name from temp_node where id=" + str(return_last_node_data_number()) )
 numrows = cursor.rowcount
 for x in range(0, numrows):
     row = cursor.fetchone()
     my_id=row[0]
 return my_id



def run_node():
 temp_data=""
 while True:
  time.sleep(0.5)
  if str(last_node_gelen_data()) !=str(last_gelen_data() ):
   print('1')
   last_st=last_status()
   last_cr=last_counter()
   if str(last_st)=='-1':
    last_cr='0'
   cursor=connection_mysql()
   insert_cumlesi="insert into chats (gelen,status,counter,giden) VALUES ('"+str(last_node_gelen_data()).lower()+"','"+str(last_st).lower()+"','"+str(last_cr).lower()+"','1')"
   print(str(insert_cumlesi))
   cursor.execute(str(insert_cumlesi))
   cursor.execute("commit")
  #success = execute_js('our-node.js')
  call(["node", "our-node.js"])
  print(temp_data)
  print(node_push_data_kontrol())
    if str(temp_data)!=str(node_push_data_kontrol()):
		call(["node","push_node.js"])
  call(["killall" ,"node"])
  temp_data=node_push_data_kontrol()
def node_push_data_kontrol():
  cursor=connection_mysql()
  cursor.execute("select giden from chats where soruid=" + str(return_last_data_number()) )
  numrows = cursor.rowcount
  for x in range(0, numrows):
     row = cursor.fetchone()
     my_id=row[0]
  print(my_id)
  return my_id



