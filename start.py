import sqlite3
from telethon import TelegramClient
import time
import subprocess
import sys
import json

db = sqlite3.connect('Account.db', timeout=30)
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Account (
    ID INTEGER PRIMARY KEY,
    API_ID TEXT,
    API_HASH TEXT,
    NAME TEXT,
    ID_SOB TEXT,
    MY_ID TEXT
)""")

db.commit()
def console_picture():
    print("")
    print("╔═══╗╔═══╗╔═══╗  ╔═══╗╔═══╗╔═══╗╔═╗╔═╗")
    print("║╔═╗║║╔═╗║║╔═╗║  ║╔═╗║║╔═╗║║╔═╗║║ ╚╝ ║")
    print("║║ ║║║║ ╚╝║╚══╗  ║║ ╚╝║╚═╝║║║ ║║║╔╗╔╗║")
    print("║║ ║║║║╔═╗╚══╗║  ║║╔═╗║╔╗╔╝║╚═╝║║║║║║║")
    print("║╚═╝║║╚╩═║║╚═╝║╔╗║╚╩═║║║║╚╗║╔═╗║║║║║║║")
    print("╚═══╝╚═══╝╚═══╝╚╝╚═══╝╚╝╚═╝╚╝ ╚╝╚╝╚╝╚╝")
    print("")    
    time.sleep(1.5)
console_picture()
print("Важно!: ")
print("1.Вы и собеседник заранее должны договориться о пароле!")
print("2.Должны быть установлены все зависимости!")
print("3.В процессе конфигурирования нужно создать 2 клиента, поэтому логиниться придеться дважды!")
print("==============================")
print("Нажми Enter чтобы запустить...")
input()

api_id = input("Введи свой Api_id: ")
api_hash = input("Введи свой Api_hash: ")
name = input("Введи ник собеседника? ")
passworld = input("Введи общий пароль, с вашим собеседником: ")
id_sob = "1"
my_id = "1"

with open("1.json") as f:
	data = f.read()
d = json.loads(data)
d["password"] = passworld
with open("1.json", 'w') as f:
	f.write(json.dumps(d))
       
with open("2.json") as f2:
	data2 = f2.read()
d2 = json.loads(data2)
d2["password"] = passworld
with open("2.json", 'w') as f2:
	f2.write(json.dumps(d2))

cur.execute(f"SELECT API_ID FROM Account WHERE API_ID = '{api_id}'")
if cur.fetchone() is None:
    cur.execute("""INSERT INTO Account(API_ID, API_HASH, NAME, ID_SOB, MY_ID) VALUES (?,?,?,?,?);""", (api_id, api_hash, name, id_sob, my_id))
    db.commit()
    print("Зарегистрированно!")


z = 1

while(True):
	session = "anon3" + str(z)
	client = TelegramClient(session, api_id, api_hash)
	client.start()
	print("Аккаунт: " + str(z) + " Вход выполнен успешно!")
	z = z+1
	if z == 3:
		print("Aккаунты активированы!")
		break
		

