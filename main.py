import discord

from discord import *

import wavelink

bot = discord.Bot()

async def connect_nodes():
    await bot.wait_until_ready()
    node = await wavelink.NodePool.create_node(
        bot=bot,
        host="bot-5.nekocat.info",
        port=2333,
        password='youshallnotpass'
        #password=""
    )
    # node.set_volume = 0.1


@bot.slash_command()
async def play(ctx, url: str):
    vc = ctx.voice_client
    # if not vc:  # check if the bot is not in a voice channel
    vc:wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)  # connect to the voice channel
    await vc.set_volume(2)
    if ctx.author.voice.channel.id != vc.channel.id:  # check if the bot is not in the voice channel
        return await ctx.respond("BOTと同じボイスチャンネルにいる必要があります！")  # return an error message
    # if "soundcloud" in url:
    # else:
    song = await wavelink.YouTubeTrack.search(query=url, return_first=True)
    # song = await wavelink.SoundCloudTrack.search(query=url, return_first=True)


    if not song:  # check if the song is not found
        return await ctx.respond("該当なし.")  # return an error message
    # wavelink.Player.volume = 0.3
    # source2 = PCMVolumeTransformer(song, 0.1)
    # song2=FFmpegPCMAudio
    # await song.convert(ctx,song2)
    # vc.client.volume = 0.1

    await vc.play(song)  # play the songe
    await ctx.respond(f"再生中: `{vc.source.title}`")  # return a message
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
@bot.event
async def on_ready():
  await connect_nodes() # connect to the server

@bot.event
async def on_wavelink_node_ready(node: wavelink.Node):
  print(f"{node.identifier} is ready.") # print a message


bot.run("ODg5NzUxNDYyODM2NTY4MDk2.G-flGO.gNzt9eMbBx4Y48ckTcAYJhkJEQpf8kc6lkNGOo")
