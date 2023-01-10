import discord

from discord import *

import wavelink

bot = discord.Bot()


#
@bot.slash_command()
async def play(ctx: ApplicationContext):
    #discord.opus.load_opus("/opt/homebrew/lib/libopus.dylib")
    vc:VoiceClient = await ctx.user.voice.channel.connect()
    source = discord.FFmpegPCMAudio("VR - Virtual Reality (Music Only) _ KMNZ [Official Music Video]-lYQGWVSVl_Y.mp3")
    source2 = PCMVolumeTransformer(source, 0.1)
    vc.play(source2)



bot.run("MTAyMTY3NDYxODY4MTAzMjcyNA.Gx2Kc4.EAEFziBXq-rHVFQkZlJ8bXbGJ120Abvod-3aj8")
