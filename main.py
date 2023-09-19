import os
import discord
import lavaplay
from discord import *
from discord import Intents
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("DISCORD_TOKEN")
intents: Intents = discord.Intents.all()
# bot = discord.Bot(intents=intents)

class MyClient(discord.Bot):
    def __init__(self, *args, intents: discord.Intents, **options):
        super().__init__(intents=intents)
        lava = lavaplay.Lavalink()

        self.lavalink = lava.create_node(
            host="risaton.net",
            port=2333,
            password="yukilava",
            user_id=123
        )
    async def setup_hook(self):
        self.lavalink.user_id = bot.user.id
        self.lavalink.set_event_loop(bot.loop)
        self.lavalink.connect()
bot = MyClient(intents=discord.Intents.all())
lavalink = bot.lavalink
@bot.event
async def on_ready():
    # await connect_nodes()  # connect to the server
    print(f"Logged in as: {bot.user.name}")
    print("Connecting following guilds:")
    for x in bot.guilds:
        print(x)
    print("--------------------------")
    print("Connecting to node...")

@lavalink.listen(lavaplay.ReadyEvent)
async def on_lava_ready(event: lavaplay.ReadyEvent):
    print("Connected to node.")
# bot.load_extension("musiccog")


# @bot.event
# async def on_wavelink_node_ready(node):
#     print("Lava is ready.")
#     print(f"{node.stats} is ready.")  # print a message
bot.run(TOKEN)
