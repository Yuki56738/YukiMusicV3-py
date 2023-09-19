import os
import discord
from discord import *
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.environ.get("DISCORD_TOKEN")
intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

"""
import wavelink
async def connect_nodes():
    await bot.wait_until_ready()
    node = await wavelink.NodePool.create_node(
        bot=bot,
        host="risaton.net",
        port=2333,
        password="yukilava",
        https=False
    )
@bot.event
async def on_voice_update(member: Member, before: VoiceState, after: VoiceState):
    if len(before.channel.members) == 1:
        await before.channel.guild.voice_client.disconnect()
song_queue = {}
async def on_song_end(guild_id: int, vc: wavelink.Player):
    song_queue[guild_id].pop(0)
    if song_queue[guild_id]:
        await vc.play(song_queue[guild_id][0])
@bot.slash_command()
async def play(ctx: ApplicationContext, url: str):
    vc = ctx.voice_client
    await ctx.defer()
    if not vc:
        vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        await vc.set_volume(2)
    if ctx.author.voice.channel.id != vc.channel.id:
        return await ctx.followup.send("BOTと同じボイスチャンネルにいる必要があります！")
    # if len(vc.channel.members) == 0:
    #     await vc.disconnect()
    song = await wavelink.YouTubeTrack.search(query=url, return_first=True)
    if not song:
        return await ctx.followup.send("該当なし.")
    if ctx.guild_id not in song_queue:
        song_queue[ctx.guild_id] = {}
    song_queue[ctx.guild_id].append(song)
    if len(song_queue[ctx.guild_id]) == 1:
        await vc.play(song_queue[ctx.guild_id][0])
        await ctx.followup.send(f"再生中: `{vc.source.title}`")
    else:
        await ctx.followup.send(f"`{song.title}` をキューに追加しました。")
    while vc.is_playing():
        await asyncio.sleep(1)
    await on_song_end(ctx.guild_id, vc)
@bot.slash_command()
async def skip(ctx: ApplicationContext):
    await ctx.defer()
    vc = ctx.voice_client
    if not vc or not vc.is_playing():
        return await ctx.followup.send("現在再生中の曲がありません。")
    vc.stop()
    if len(song_queue[ctx.guild_id]) > 0:  # if there are other songs in the queue, play the next one
        song = song_queue.pop(0)
        await vc.play(song)
        await ctx.followup.send(f"再生中: `{vc.source.title}`")
    else:  # if the queue is empty, disconnect from the voice channel
        await vc.disconnect()
        await ctx.followup.send("曲が終了しました。")
@bot.slash_command()
async def stop(ctx: ApplicationContext):
    vc = ctx.voice_client
    await vc.disconnect()
    await ctx.respond(embed=Embed(description="Disconnecting..."))
    song_queue[ctx.guild_id] = []
@bot.event
"""
async def on_ready():
    # await connect_nodes()  # connect to the server
    print(f"Logged in as: {bot.user.name}")
    print("Connecting following guilds:")
    for x in bot.guilds:
        print(x)
    print("--------------------------")
bot.load_extension("musiccog")


# @bot.event
# async def on_wavelink_node_ready(node):
#     print("Lava is ready.")
#     print(f"{node.stats} is ready.")  # print a message
bot.run(TOKEN)
