import os

import discord

from discord import *

import wavelink

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("DISCORD_TOKEN")

bot = discord.Bot()


async def connect_nodes():
    await bot.wait_until_ready()
    node = await wavelink.NodePool.create_node(
        bot=bot,
        host="34.133.23.172",
        port=2333,
        password='youshallnotpass'
        # password=""
    )
    # node.set_volume = 0.1

@bot.event
async def on_voice_update(member: Member, before: VoiceState, after: VoiceState):
    vc = before.voice_client
    if len(before.channel.members)==1:
        await before.channel.guild.voice_client.disconnect()
song_queue = {}  # initialize the song queue as an empty dictionary

async def on_song_end(guild_id: int, vc: wavelink.Player):
    # remove the finished song from the queue
    global song_queue
    song_queue[guild_id].pop(0)

    # if there are more songs in the queue, play the next one
    if song_queue[guild_id]:
        await vc.play(song_queue[guild_id][0])
    else:
        # if the queue is empty, disconnect from the voice channel
        await vc.disconnect()

@bot.slash_command()
async def play(ctx: ApplicationContext, url: str):
    vc = ctx.voice_client
    await ctx.defer()
    if not vc:
        vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        await vc.set_volume(2)
    if ctx.author.voice.channel.id != vc.channel.id:
        return await ctx.followup.send("BOTと同じボイスチャンネルにいる必要があります！")
    if len(vc.channel.members)==0:
        await vc.disconnect()

    song = await wavelink.YouTubeTrack.search(query=url, return_first=True)

    if not song:
        return await ctx.followup.send("該当なし.")
    global song_queue
    if ctx.guild_id not in song_queue:
        song_queue[ctx.guild_id] = []  # initialize the queue for the guild if it doesn't exist
    song_queue[ctx.guild_id].append(song)  # add the song object to the end of the queue

    if len(song_queue[ctx.guild_id]) == 1:  # if this is the first song in the queue, play it
        await vc.play(song_queue[ctx.guild_id][0])
        await ctx.followup.send(f"再生中: `{vc.source.title}`")
    else:  # if there are other songs in the queue, just add it to the queue
        await ctx.followup.send(f"`{song.title}` をキューに追加しました。")

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


#
# @bot.slash_command()
# async def play(ctx: ApplicationContext):
#     #discord.opus.load_opus("/opt/homebrew/lib/libopus.dylib")
#     vc:VoiceClient = await ctx.user.voice.channel.connect()
#     source = discord.FFmpegPCMAudio("VR - Virtual Reality (Music Only) _ KMNZ [Official Music Video]-lYQGWVSVl_Y.mp3")
#     source2 = PCMVolumeTransformer(source, 0.1)
#     vc.play(source2)

@bot.slash_command()
async def stop(ctx: ApplicationContext):
    vc = ctx.voice_client
    await vc.disconnect()
    await ctx.respond(embed=Embed(description="Disconnecting..."))
    song_queue[ctx.guild_id] = {}


@bot.event
async def on_ready():
    await connect_nodes()  # connect to the server


@bot.event
async def on_wavelink_node_ready(node: wavelink.Node):
    print(f"{node.identifier} is ready.")  # print a message


bot.run(TOKEN)