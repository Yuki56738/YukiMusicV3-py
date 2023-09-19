import os

import hikari
import lavaplay
from dotenv import load_dotenv
load_dotenv()

bot = hikari.GatewayBot(os.environ.get("DISCORD_TOKEN"))

lavalink = lavaplay.Lavalink()
node = lavalink.create_node(
    host="risaton.net",
    port=2333,
    password="yukilava",
    user_id=123
)

@bot.listen()
async def on_ready(event: hikari.ShardReadyEvent):
    print("Connecting to node...")
    node.connect()

bot.run()