import os
import discord
import lavaplay
from discord import *
from discord import Intents
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("DISCORD_TOKEN")
intents: Intents = discord.Intents.all()
bot = discord.Bot(intents=intents)




lava = lavaplay.Lavalink()

lavalink = lava.create_node(
    host="risaton.net",
    port=2333,
    password="yukilava",
    user_id=123
)

@bot.event
async def on_ready():
    # await connect_nodes()  # connect to the server
    print(f"Logged in as: {bot.user.name}")
    print("Connecting following guilds:")
    for x in bot.guilds:
        print(x)
    print("--------------------------")
    print("Connecting to node...")
    global lavalink
    lavalink.user_id = bot.user.id
    lavalink.set_event_loop(bot.loop)
    lavalink.connect()


@lavalink.listen(lavaplay.ReadyEvent)
async def on_lava_ready(event: lavaplay.ReadyEvent):
    print("Connected to node.")
# bot.load_extension("musiccog")


# @bot.event
# async def on_wavelink_node_ready(node):
#     print("Lava is ready.")
#     print(f"{node.stats} is ready.")  # print a message
bot.run(TOKEN)
