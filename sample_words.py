#!/usr/bin/env python
# -*- coding: utf-8 -*-


import my_sql_operations as todb
import MySQLdb

def bakiye_sorgu():
  try:
   cursor=connection_mysql()
   cumle="select hesap_bakiyesi from  bankacilik_islemleri limit 1"
   cursor.execute(str(cumle))
   numrows = cursor.rowcount
   for x in range(0, numrows):
     row = cursor.fetchone()
     return row[0]
  except:
   pass

def bakiye_azalt(para):
  try:
   print(str(para)+ ' gelen para')
   guncel_bakiye=bakiye_sorgu()
   print(str(guncel_bakiye)+ ' bakiye guncel')
   guncellenecek=int(guncel_bakiye)-int(para)
   cursor=connection_mysql()
   cumle="UPDATE bankacilik_islemleri SET hesap_bakiyesi = '"+str(guncellenecek)+"'"
   cursor.execute(str(cumle))
   cursor.execute("commit")
   return guncellenecek
  except:
   pass

def get_writen_text(my_id):
  try:
   cursor=connection_mysql()
   cursor.execute("select gelen from chats where soruid="+ str(my_id)+"")
   numrows = cursor.rowcount
   for x in range(0, numrows):
     row = cursor.fetchone()
     return row[0]
  except:
   pass
def eft_sorgu(ad,para,kart_no,tip):
 try:
  cursor=connection_mysql()
  if tip=='1':
   cumle="UPDATE bankacilik_islemleri SET eft_gonderilecek_ad = '"+str(ad)+"'"
  if tip=='2':
   cumle="UPDATE bankacilik_islemleri SET eft_gonderilecek_para = '"+str(para)+"' "
  cursor.execute(str(cumle))
  para=0
  cursor.execute("commit")
  if tip=='2':
   cursor.execute("select eft_gonderilecek_ad from bankacilik_islemleri limit 1 ")
   numrows = cursor.rowcount
   for x in range(0, numrows):
      row = cursor.fetchone()
      return row[0],para
  else:
   return ad,para
 except :
  pass
def connection_mysql():
 db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="mysql",
                     db="albaraka")

 cursor = db.cursor()
 return cursor

def gonderilen_getir():
  cursor=connection_mysql()
  cursor.execute("select eft_gonderilecek_ad from bankacilik_islemleri limit 1 ")
  numrows = cursor.rowcount
  for x in range(0, numrows):
     row = cursor.fetchone()
     return row[0]

def para_cekme_api(my_id):
  todb.insert_to_bot('Ne kadar cekmek istiyorsunuz ?',my_id)

def eft_api(my_id):
 counter=todb.get_current_counter(my_id)
 if str(counter)=='0':
  print('Neden')
  todb.insert_to_bot('Kime para gondermek istiyorsunuz ?',my_id,1,0)
 if str(counter)=='1':
  tip='1'
  para=0
  kart_no='0'
  ad=get_writen_text(my_id)
                                                                                                           136,1         34%
  test,para=eft_sorgu(str(ad),para,kart_no,tip)
  todb.insert_to_bot(str(ad)+' kisisine kac para gondermek istiyorsunuz  ?',my_id,1,0)
 if str(counter)=='2':
  tip='2'
  para='0'
  kart_no='0'
  para=get_writen_text(my_id)
  print('para '+ str(para))
  my_id=int(my_id)-1
  ad=get_writen_text(my_id)
  print(str(ad)+ ' addd')
  test,param=eft_sorgu(ad,para,kart_no,tip)
  kalan_bakiye=bakiye_azalt(para)
  my_id=my_id+1
  todb.insert_to_bot(str(ad)+ '  hesap numarali Beyhan GUL kisisine '+str(para)+' TL lik isleminiz onaylandi! Kalan bakiyeniz '+str(kalan_bakiye)+' tl dir',my_id,1,1)

def bakiye_sorgulama_api(my_id):
 try:
  counter=todb.get_current_counter(my_id)
  if str(counter)=='0':
   print('Neden')
   todb.insert_to_bot('Bakiyenizi mi ogrenmek istiyorsunuz ?',my_id,4,0)
  if str(counter)=='1':
   todb.insert_to_bot('Hangi hesap numaraniz ?',my_id,4,0)
  if str(counter)=='2':
   bakiyem=bakiye_sorgu()
   todb.insert_to_bot('Bakiyeniz... '+ str(bakiyem)+  ' TL dir',my_id,4,1)
 except:
  pass
def limit_ogren():
  cursor=connection_mysql()
  cursor.execute("select kredi_karti_limit from bankacilik_islemleri limit 1 ")
  numrows = cursor.rowcount
  for x in range(0, numrows):
     row = cursor.fetchone()
     return row[0]

def limit_artir(artacak):
 limit_artisi=int(limit_ogren())+int(artacak)
 cursor=connection_mysql()
 cumle="UPDATE bankacilik_islemleri SET kredi_karti_limit = '"+str(limit_artisi)+"'"
 cursor.execute(str(cumle))
 cursor.execute("commit")


def kredi_karti_limit_arttirim(my_id):
 try:
  counter=todb.get_current_counter(my_id)
  if str(counter)=='0':
   print('Neden')
   todb.insert_to_bot('Limitini arttirmak istediginiz kart numarasi nedir ?',my_id,7,0)
  if str(counter)=='1':
   todb.insert_to_bot('Limitiniz '+str(limit_ogren())+' Kac TL arttirmak istiyorsunuz ? ',my_id,7,0)
  if str(counter)=='2':

   limit_artir(get_writen_text(my_id))
   todb.insert_to_bot('Limitiniz onaylanmistir. Yeni kart limitiniz '+str(limit_ogren()) +'TL',my_id,7,1)
 except:
  pass
def kredi_taksit_hesaplama():
   cursor=connection_mysql()
   cumle="select  from  bankacilik_islemleri limit 1"
   cursor.execute(str(cumle))
   numrows = cursor.rowcount
   for x in range(0, numrows):
     row = cursor.fetchone()
     return row[0]