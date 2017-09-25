import MySQLdb

def connection_mysql():
 db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="mysql",
                     db="albaraka")

 cursor = db.cursor()
 return cursor

def eft_sorgu(ad,para,kart_no,tip):
 cursor=connection_mysql()
 if tip=='1':
  cumle="UPDATE bankacilik_islemleri SET gonderilecek_ad = '"+str(coming_text)+"'  WHERE kart_no = "+ str(kart_no)
 if tip=='2':
  cumle="UPDATE bankacilik_islemleri SET gonderilecek_para = '"+str(coming_text)+"'  WHERE kart_no = "+ str(kart_no)
 cursor.execute(str(cumle))
 cursor.execute("commit")
 cursor.execute("select gonderilecek_ad from bankacilik_islemleri limit 1 ")
 numrows = cursor.rowcount
 for x in range(0, numrows):
     row = cursor.fetchone()
     return row[0],coming_text

def bakiye_azalt(para):
   guncel_bakiye=bakiye_sorgu()
   guncellenecek=int(guncel_bakiye)-int(para)
   cursor=connection_mysql()
   cumle="UPDATE bankacilik_islemleri SET hesap_bakiyesi = '"+str(guncellenecek)+"'"
   cursor.execute(str(cumle))
   cursor.execute("commit")
   return guncellenecek




def get_writen_text(my_id):
   cursor=connection_mysql()
   my_id=int(my_id)-1
   cursor.execute("select gelen from chats where soruid="+ str(my_id)+"")
   numrows = cursor.rowcount
   for x in range(0, numrows):
     row = cursor.fetchone()
     return row[0]


def get_current_counter(soruid):
   cursor=connection_mysql()
   cursor.execute("select counter from chats where soruid="+ str(soruid)+"")
   numrows = cursor.rowcount
   for x in range(0, numrows):
     row = cursor.fetchone()
     my_counter=row[0]
   return my_counter
def insert_to_bot(coming_text,soruid,status_id,islem_sonu):
  cursor=connection_mysql()
  cursor.execute("select counter from chats where soruid="+ str(soruid)+"")
  numrows = cursor.rowcount
  for x in range(0, numrows):
     row = cursor.fetchone()
     my_counter=row[0]
  my_counter=int(my_counter)+1
  if str(islem_sonu)=='1':
   my_counter=-1
   status_id=-1
  cumle="UPDATE chats SET giden = '"+str(coming_text)+"', status= "+str(status_id)+",counter='"+str(my_counter)+"'  WHERE soruid = "+ str(soruid)
  print(str(cumle))
  cursor.execute(str(cumle))
  cursor.execute("commit")
  #cursor.execute("UPDATE chats SET giden = "+str(coming_text)+"  WHERE soruid = "+ str(soruid))

  cursor.close()
