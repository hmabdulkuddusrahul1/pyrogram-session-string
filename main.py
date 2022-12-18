import os
from pyrogram import Client
from pyrogram.errors import SessionPasswordNeeded
app = Client("idkkkk", 9398500, "ad2977d673006bed6e5007d953301e13", in_memory=True)

app.connect()

phone = input("Enter Your phone number : ")
a = app.send_code(phone)
hash = a.phone_code_hash
code = input("Enter the code you recived : ")
try:
  app.sign_in(phone, hash, code)
except SessionPasswordNeeded:
 password = input("Enter your password : ")
 app.check_password(password=password)
 
app.sign_in(phone, hash, code)
string_session = app.export_session_string()
os.system("clear")
print("\n\n"+string_session)

app.disconnect()
