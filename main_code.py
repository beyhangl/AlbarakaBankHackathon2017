import MySQLdb
import time
import chatterbotum as get_result
from chatterbot import ChatBot
import hazir_cumleler as banka_getir
import my_sql_operations as ancon



def connection_mysql():
 db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="mysql",
                     db="albaraka")

 cursor = db.cursor()
 return cursor

def return_last_data_number():
 cursor=connection_mysql()
 cursor.execute("select max(soruid) from chats")
 numrows = cursor.rowcount
 for x in range(0, numrows):
     row = cursor.fetchone()
     my_id=row[0]
 return my_id

def hazir_banka_sorulari(gelen_text,my_id):
  encoder_words=["Para cekme istiyor","Eft yapacak", "Konumunu paylas","En yakin atm goster","Bakiye sorgula","Doviz bilgileri","Fatura Odeme","Kredi karti limit arttir","Kredi basvurusu yapacak"]
  splitted=gelen_text.split()
  #print('As')
  sonuc,kac_tane = banka_getir.banka_textleri(gelen_text)
   #banka_getir.yardir(my_id,gelen_text)
  #if sonuc==0:
  # banka_getir.para_cekme_api(my_id)
  if sonuc==1:
   banka_getir.eft_api(my_id)
 # if sonuc==2:
 #  banka_getir.konumunu_at_api()
 # if sonuc==3:
 #  banka_getir.en_yakin_atm_api()
  if sonuc==4:
   banka_getir.bakiye_sorgulama_api(my_id)
  if sonuc==5:
   banka_getir.doviz_bilgisi_api(my_id)
  if sonuc==6:
   banka_getir.fatura_odeme(my_id)
  if sonuc==7:
   banka_getir.kredi_karti_limit_arttirim(my_id)
  #if sonuc==8:
def last_data_status(my_id):
  last_id=int(my_id)
  cursor=connection_mysql()
  cursor.execute("select status from chats where soruid =  "+ str(last_id))
  numrows = cursor.rowcount
  for x in range(0, numrows):
     row = cursor.fetchone()
     gelen_text=row[0]
     return gelen_text


def my_loop():
 ##EGITIM BASLANGIC
 #chat=get_result.trainet()
 ##EGITIM BITIS
 temp_text=""
 gelen_text=""
 while True:
  time.sleep(0.5)
  my_id=return_last_data_number()
  gelen_text=return_last_coming_chat_text(my_id)
  #print(str(gelen_text))
  #print(str(temp_text))
  if (int(last_data_status(my_id))==-1) and str(temp_text)!=str(gelen_text):
   print('gir mk')
   gelen_text=return_last_coming_chat_text(my_id)
   sonuc,encoder=hazir_banka_sorulari(gelen_text,my_id)
   print(str(encoder[sonuc]))
  elif (int(last_data_status(my_id))==0) and str(temp_text)!=str(gelen_text):
   print('ZAZA')
  elif(int(last_data_status(my_id))==1 and str(temp_text)!=str(gelen_text)):
   print(str(gelen_text))
   print(str(temp_text))
   print('1')
   banka_getir.eft_api(my_id)
  elif(int(last_data_status(my_id))==4 and str(temp_text)!=str(gelen_text)):
   print(str(gelen_text))
   print(str(temp_text))
   print('1')
   banka_getir.bakiye_sorgulama_api(my_id)
  elif(int(last_data_status(my_id))==5 and str(temp_text)!=str(gelen_text)):
   print(str(gelen_text))
   print(str(temp_text))
   print('1')
   banka_getir.doviz_bilgisi_api(my_id)
  elif(int(last_data_status(my_id))==6 and str(temp_text)!=str(gelen_text)):
   print(str(gelen_text))
  temp_text=gelen_text
  ##EGITIM CAGIR
  #print(chat.get_response(str(gelen_text)))
  ##EGITIM BITIS

def return_last_coming_chat_text(my_id):
 try:
  cursor=connection_mysql()
  cursor.execute("select gelen from chats where soruid =  "+ str(my_id))
  numrows = cursor.rowcount
  for x in range(0, numrows):
     row = cursor.fetchone()
     gelen_text=row[0]
     return gelen_text
 except :
  pass
my_loop()
