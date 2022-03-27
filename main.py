import asyncio
import configparser
from pyrogram import Client, filters

config = configparser.ConfigParser()
config.read("config.ini")

api_id = config["pyrogram"]["api_id"]
api_hash = config["pyrogram"]["api_hash"]
death_group = int(config["pyrogram"]["death_group"])
room_group = int(config["pyrogram"]["room_group"])
poop_mate1 = config["pyrogram"]["poop_mate1"]
love_mate = config["pyrogram"]["love_mate"]
poop_mate2 = config["pyrogram"]["poop_mate2"]
print(room_group)
app = Client("asd")


@app.on_raw_update(group=death_group)
async def death_handler(client, update, _, __):
    for i in range(1):
        history = await app.get_history(death_group, limit=1)
        for message in history:
            print(message["from_user"]["username"])
            if message["from_user"]["username"] == love_mate:
                await app.send_reaction(death_group, message["message_id"], "❤️")
            elif message["from_user"]["username"] == poop_mate1:
                await app.send_reaction(death_group, message["message_id"], "💩")


@app.on_raw_update(group=room_group)
async def misha_handler(client, update, _, __):
    for i in range(1):
        history = await app.get_history(room_group, limit=1)
        for message in history:
            print(message["from_user"]["username"])
            if message["from_user"]["username"] == poop_mate2:
                await app.send_reaction(room_group, message["message_id"], "💩")


app.run()
